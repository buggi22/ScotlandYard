(function () {
  var app = angular.module('game', ['ScotlandYard.StandardBoard']);

  app.controller('GameCtrl', function ($scope, BoardService, $q) {
    $scope.scenario = {
      startPositionType: 'any_start_pos',
      specificStartPos: '46',
      transitType: 'taxi'
    };
    BoardService.nodes.then(function (nodes) {
      $scope.nodes = nodes;
    });

    $scope.checkPossibleDestinations = function () {
      //example for fetching route data
      var startPositions;
      if ($scope.scenario.startPositionType == 'any_start_pos') {
        startPositions = ['any_start_location'];
      } else {
        startPositions = $scope.scenario.specificStartPos.split(',');
      }
      var routes = BoardService.getRoutes(startPositions, [$scope.scenario.transitType]);
      var nodes = BoardService.nodes;
      $q.all([routes, nodes]).then(function (arr) {
        var data = arr[0];
        var nodes = arr[1];
        var locs = data.locations;
        angular.forEach(nodes, function (node, idx) {
          node.possibleMatch = false;
        });
        angular.forEach(locs, function (loc, idx) {
          BoardService.nodeNamed(loc).then(function (node) {
            node.possibleMatch = true;
            console.log(node);
          });
        });
      });
    };
  });

  app.service('BoardService', function ($http, $q, StandardBoard) {

    var self = {
      nodeNamed: function (name) {
        return self.nodes.then(function (nodes) {
          return nodes[name - 1];
        });
      },
      getRoutes: function (startLocations, transits) {
        var params = {
          starts: startLocations.join(","), 
          transits: transits.join(",")
        };
        return $http.get('/ajax', {params: params}).then(function (rsp) {
          return rsp.data;
        });
      },
      fullBoard: function () {
        //cache the promise once we make it, since this is static data
        if (!self.boardPromise) {
          self.boardPromise = $http.get('/ajax', {params: {fullboard: 1}}).then(function (rsp) {
            return rsp.data;
          });
        }
        return self.boardPromise;
      }
    };

    var rawCoords = StandardBoard.getRawCoords();
    var fullBoard = self.fullBoard();
    self.nodes = $q.all([rawCoords, fullBoard]).then(function (arr) {
      var coords = arr[0];
      var fullBoard = arr[1];

      var nodes = [];
      for (i = 0; i < coords.length/2; i++) {
        var x = coords[2*i];
        var y = coords[2*i+1];
        var name = "" + (i+1);
        nodes[nodes.length] = {
          x: x,
          y: y,
          name: name,
          routes: fullBoard.board[name]
        };
      }
      return nodes;
    });

    return self;
  });


})();
