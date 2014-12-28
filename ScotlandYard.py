#!/usr/bin/python

# Board representation adapted from https://github.com/geeksam/Scotland-Yard
FullBoard = {
  1: {
    'taxi': [8, 9],
    'bus': [58, 46],
    'underground': [46],
  },
  2: {
    'taxi': [10, 20],
  },
  3: {
    'taxi': [4, 11, 12],
    'bus': [22, 23],
  },
  4: {
    'taxi': [3, 13],
  },
  5: {
    'taxi': [15, 16],
  },
  6: {
    'taxi': [7, 29],
  },
  7: {
    'taxi': [6, 17],
    'bus': [42],
  },
  8: {
    'taxi': [1, 18, 19],
  },
  9: {
    'taxi': [1, 19, 20],
  },
  10: {
    'taxi': [2, 11, 21, 34],
  },
  11: {
    'taxi': [3, 10, 22],
  },
  12: {
    'taxi': [3, 23],
  },
  13: {
    'taxi': [4, 23, 24],
    'bus': [14, 23, 52],
    'underground': [46, 67, 89],
  },
  14: {
    'taxi': [15, 25],
    'bus': [13, 15],
  },
  15: {
    'taxi': [5, 14, 16, 26, 28],
    'bus': [14, 29, 41],
  },
  16: {
    'taxi': [5, 15, 28, 29],
  },
  17: {
    'taxi': [7, 29, 30],
  },
  18: {
    'taxi': [8, 31, 43],
  },
  19: {
    'taxi': [8, 9, 32],
  },
  20: {
    'taxi': [2, 9, 33],
  },
  21: {
    'taxi': [10, 33],
  },
  22: {
    'taxi': [11, 23, 34, 35],
    'bus': [3, 23, 34, 65],
  },
  23: {
    'taxi': [12, 13, 22, 37],
    'bus': [3, 13, 22, 67],
  },
  24: {
    'taxi': [13, 37, 38],
  },
  25: {
    'taxi': [14, 38, 39],
  },
  26: {
    'taxi': [15, 27, 39],
  },
  27: {
    'taxi': [26, 28, 40],
  },
  28: {
    'taxi': [15, 16, 27, 41],
  },
  29: {
    'taxi': [6, 16, 17, 41, 42],
    'bus': [15, 41, 42, 55],
  },
  30: {
    'taxi': [17, 42],
  },
  31: {
    'taxi': [18, 43, 44],
  },
  32: {
    'taxi': [19, 33, 44, 45],
  },
  33: {
    'taxi': [20, 21, 32, 46],
  },
  34: {
    'taxi': [10, 22, 47, 48],
    'bus': [22, 46, 63],
  },
  35: {
    'taxi': [22, 36, 48, 65],
  },
  36: {
    'taxi': [35, 37, 49],
  },
  37: {
    'taxi': [23, 24, 36, 50],
  },
  38: {
    'taxi': [24, 25, 50, 51],
  },
  39: {
    'taxi': [25, 26, 51, 52],
  },
  40: {
    'taxi': [27, 41, 52, 53],
  },
  41: {
    'taxi': [28, 29, 40, 54],
    'bus': [15, 29, 52, 87],
  },
  42: {
    'taxi': [29, 30, 56, 72],
    'bus': [7, 29, 72],
  },
  43: {
    'taxi': [18, 31, 57],
  },
  44: {
    'taxi': [31, 32, 58],
  },
  45: {
    'taxi': [32, 46, 58, 59, 60],
  },
  46: {
    'taxi': [33, 45, 47, 61],
    'bus': [1, 34, 58, 78],
    'underground': [1, 13, 74, 79],
  },
  47: {
    'taxi': [34, 46, 62],
  },
  48: {
    'taxi': [34, 35, 62, 63],
  },
  49: {
    'taxi': [36, 50, 66],
  },
  50: {
    'taxi': [37, 38, 49],
  },
  51: {
    'taxi': [38, 39, 52, 67, 68],
  },
  52: {
    'taxi': [39, 40, 51, 69],
    'bus': [13, 41, 67, 86],
  },
  53: {
    'taxi': [40, 54, 69],
  },
  54: {
    'taxi': [41, 53, 55, 70],
  },
  55: {
    'taxi': [54, 71],
    'bus': [29, 89],
  },
  56: {
    'taxi': [42, 91],
  },
  57: {
    'taxi': [43, 58, 73],
  },
  58: {
    'taxi': [44, 45, 57, 59, 74, 75],
    'bus': [1, 46, 74, 77],
  },
  59: {
    'taxi': [45, 58, 75, 76],
  },
  60: {
    'taxi': [45, 61, 76],
  },
  61: {
    'taxi': [46, 60, 62, 76, 78],
  },
  62: {
    'taxi': [47, 48, 61, 79],
  },
  63: {
    'taxi': [48, 64, 79, 80],
    'bus': [34, 65, 79, 100],
  },
  64: {
    'taxi': [63, 65, 81],
  },
  65: {
    'taxi': [35, 64, 66, 82],
    'bus': [22, 63, 67, 82],
  },
  66: {
    'taxi': [49, 65, 67, 82],
  },
  67: {
    'taxi': [51, 66, 68, 84],
    'bus': [23, 52, 65, 82, 102],
    'underground': [13, 79, 89, 111],
  },
  68: {
    'taxi': [51, 67, 69, 85],
  },
  69: {
    'taxi': [52, 53, 68, 86],
  },
  70: {
    'taxi': [54, 71, 87],
  },
  71: {
    'taxi': [55, 70, 72, 89],
  },
  72: {
    'taxi': [42, 71, 90, 91],
    'bus': [42, 105, 107],
  },
  73: {
    'taxi': [57, 74, 92],
  },
  74: {
    'taxi': [58, 73, 75, 92],
    'bus': [58, 94],
    'underground': [46],
  },
  75: {
    'taxi': [58, 59, 74, 94],
  },
  76: {
    'taxi': [59, 60, 61, 77],
  },
  77: {
    'taxi': [76, 78, 95, 96],
    'bus': [58, 78, 94, 124],
  },
  78: {
    'taxi': [61, 77, 79, 97],
    'bus': [46, 77, 79],
  },
  79: {
    'taxi': [62, 63, 78, 98],
    'bus': [78, 63],
    'underground': [46, 67, 93, 111],
  },
  80: {
    'taxi': [63, 99, 100],
  },
  81: {
    'taxi': [64, 82, 100],
  },
  82: {
    'taxi': [65, 66, 81, 101],
    'bus': [65, 67, 100, 140],
  },
  83: {
    'taxi': [101, 102],
  },
  84: {
    'taxi': [67, 85],
  },
  85: {
    'taxi': [68, 84, 103],
  },
  86: {
    'taxi': [69, 103, 104],
    'bus': [52, 87, 102, 116],
  },
  87: {
    'taxi': [70, 88],
    'bus': [41, 86, 105],
  },
  88: {
    'taxi': [87, 89, 117],
  },
  89: {
    'taxi': [71, 88, 105],
    'bus': [55, 105],
    'underground': [13, 67, 128, 140],
  },
  90: {
    'taxi': [72, 91, 105],
  },
  91: {
    'taxi': [56, 72, 90, 105, 107],
  },
  92: {
    'taxi': [73, 74, 93],
  },
  93: {
    'taxi': [92, 94],
    'bus': [94],
    'underground': [79],
  },
  94: {
    'taxi': [75, 93, 95],
    'bus': [74, 77, 93],
  },
  95: {
    'taxi': [77, 94, 122],
  },
  96: {
    'taxi': [77, 97, 109],
  },
  97: {
    'taxi': [78, 96, 98, 109],
  },
  98: {
    'taxi': [79, 97, 99, 110],
  },
  99: {
    'taxi': [80, 98, 110],
  },
  100: {
    'taxi': [80, 81, 101, 112, 113],
    'bus': [63, 82, 111],
  },
  101: {
    'taxi': [82, 83, 100, 114],
  },
  102: {
    'taxi': [83, 103, 115],
    'bus': [67, 86, 127],
  },
  103: {
    'taxi': [85, 86, 102],
  },
  104: {
    'taxi': [86, 116],
  },
  105: {
    'taxi': [89, 90, 91, 106, 108],
    'bus': [72, 87, 89, 107, 108],
  },
  106: {
    'taxi': [105, 107],
  },
  107: {
    'taxi': [91, 106, 119],
    'bus': [72, 105, 161],
  },
  108: {
    'taxi': [105, 117, 119],
    'bus': [105, 116, 135],
    'river': [115],
  },
  109: {
    'taxi': [96, 97, 110, 124],
  },
  110: {
    'taxi': [98, 99, 109, 111],
  },
  111: {
    'taxi': [110, 112, 124],
    'bus': [100, 124],
    'underground': [67, 79, 153, 163],
  },
  112: {
    'taxi': [100, 111, 125],
  },
  113: {
    'taxi': [100, 114, 125],
  },
  114: {
    'taxi': [101, 113, 115, 126, 131, 132],
  },
  115: {
    'taxi': [102, 114, 126, 127],
    'river': [108, 157],
  },
  116: {
    'taxi': [104, 117, 118, 127],
    'bus': [86, 108, 127, 142],
  },
  117: {
    'taxi': [88, 108, 116, 129],
  },
  118: {
    'taxi': [116, 129, 134, 142],
  },
  119: {
    'taxi': [107, 108, 136],
  },
  120: {
    'taxi': [121, 144],
  },
  121: {
    'taxi': [120, 122, 145],
  },
  122: {
    'taxi': [95, 121, 123, 146],
    'bus': [123, 144],
  },
  123: {
    'taxi': [122, 124, 137, 148, 149],
    'bus': [122, 124, 144, 165],
  },
  124: {
    'taxi': [109, 111, 123, 130, 138],
    'bus': [77, 111, 123, 153],
  },
  125: {
    'taxi': [112, 113, 131],
  },
  126: {
    'taxi': [114, 115, 127, 140],
  },
  127: {
    'taxi': [115, 116, 126, 133, 134],
    'bus': [102, 116, 133],
  },
  128: {
    'taxi': [142, 143, 160, 172, 188],
    'bus': [135, 142, 161, 187, 199],
    'underground': [89, 140, 185],
  },
  129: {
    'taxi': [117, 118, 135, 142, 143],
  },
  130: {
    'taxi': [124, 131, 139],
  },
  131: {
    'taxi': [114, 125, 130],
  },
  132: {
    'taxi': [114, 140],
  },
  133: {
    'taxi': [127, 140, 141],
    'bus': [127, 140, 157],
  },
  134: {
    'taxi': [118, 127, 141, 142],
  },
  135: {
    'taxi': [129, 136, 143, 161],
    'bus': [108, 128, 161],
  },
  136: {
    'taxi': [119, 135, 162],
  },
  137: {
    'taxi': [123, 147],
  },
  138: {
    'taxi': [124, 150, 152],
  },
  139: {
    'taxi': [130, 140, 153, 154],
  },
  140: {
    'taxi': [126, 132, 133, 139, 154, 156],
    'bus': [82, 133, 154, 156],
    'underground': [89, 128, 153],
  },
  141: {
    'taxi': [133, 134, 142, 158],
  },
  142: {
    'taxi': [118, 128, 129, 134, 141, 143, 158],
    'bus': [116, 128, 157],
  },
  143: {
    'taxi': [128, 129, 135, 142, 160],
  },
  144: {
    'taxi': [120, 145, 177],
    'bus': [122, 123, 163],
  },
  145: {
    'taxi': [121, 144, 146],
  },
  146: {
    'taxi': [122, 145, 147, 163],
  },
  147: {
    'taxi': [137, 146, 164],
  },
  148: {
    'taxi': [123, 149, 164],
  },
  149: {
    'taxi': [123, 148, 150, 165],
  },
  150: {
    'taxi': [138, 149, 151],
  },
  151: {
    'taxi': [150, 152, 165, 166],
  },
  152: {
    'taxi': [138, 151, 153],
  },
  153: {
    'taxi': [139, 152, 154, 166, 167],
    'bus': [124, 154, 180, 184],
    'underground': [111, 140, 163, 185],
  },
  154: {
    'taxi': [139, 140, 153, 155],
    'bus': [140, 153, 156],
  },
  155: {
    'taxi': [154, 156, 167, 168],
  },
  156: {
    'taxi': [140, 155, 157, 169],
    'bus': [140, 154, 157, 184],
  },
  157: {
    'taxi': [156, 158, 170],
    'bus': [156, 133, 142, 185],
    'river': [115, 194],
  },
  158: {
    'taxi': [141, 142, 157, 159],
  },
  159: {
    'taxi': [158, 170, 172, 186],
  },
  160: {
    'taxi': [128, 143, 161, 173],
  },
  161: {
    'taxi': [135, 160, 174],
    'bus': [107, 128, 135, 199],
  },
  162: {
    'taxi': [136, 175],
  },
  163: {
    'taxi': [146, 177],
    'bus': [144, 176, 191],
    'underground': [111, 153],
  },
  164: {
    'taxi': [147, 148, 178, 179],
  },
  165: {
    'taxi': [149, 151, 179, 180],
    'bus': [123, 180, 191],
  },
  166: {
    'taxi': [151, 153, 181, 183],
  },
  167: {
    'taxi': [153, 155, 168, 183],
  },
  168: {
    'taxi': [155, 167, 184],
  },
  169: {
    'taxi': [156, 184],
  },
  170: {
    'taxi': [157, 159, 185],
  },
  171: {
    'taxi': [173, 175, 199],
  },
  172: {
    'taxi': [128, 159, 187],
  },
  173: {
    'taxi': [160, 171, 174, 188],
  },
  174: {
    'taxi': [161, 173, 175],
  },
  175: {
    'taxi': [162, 174, 171],
  },
  176: {
    'taxi': [177, 189],
    'bus': [163, 190],
  },
  177: {
    'taxi': [144, 163, 176],
  },
  178: {
    'taxi': [164, 189, 191],
  },
  179: {
    'taxi': [164, 165, 191],
  },
  180: {
    'taxi': [165, 181, 193],
    'bus': [153, 165, 190, 184],
  },
  181: {
    'taxi': [166, 180, 182, 193],
  },
  182: {
    'taxi': [181, 183, 195],
  },
  183: {
    'taxi': [166, 167, 182, 196],
  },
  184: {
    'taxi': [168, 169, 185, 196, 197],
    'bus': [153, 156, 180, 185],
  },
  185: {
    'taxi': [170, 184, 186],
    'bus': [157, 184, 187],
    'underground': [128, 153],
  },
  186: {
    'taxi': [185, 159, 198],
  },
  187: {
    'taxi': [172, 188, 198],
    'bus': [128, 185],
  },
  188: {
    'taxi': [128, 173, 187, 199],
  },
  189: {
    'taxi': [176, 178, 190],
  },
  190: {
    'taxi': [189, 191, 192],
    'bus': [176, 180, 191],
  },
  191: {
    'taxi': [178, 179, 190, 192],
    'bus': [163, 165, 190],
  },
  192: {
    'taxi': [190, 191, 194],
  },
  193: {
    'taxi': [180, 181, 194],
  },
  194: {
    'taxi': [192, 193, 195],
    'river': [157],
  },
  195: {
    'taxi': [182, 194, 197],
  },
  196: {
    'taxi': [183, 184, 197],
  },
  197: {
    'taxi': [184, 195, 196],
  },
  198: {
    'taxi': [186, 187, 199],
  },
  199: {
    'taxi': [171, 188, 198],
    'bus': [128, 161],
  },
}

TAXI = set(['taxi'])
BUS = set(['bus'])
UNDERGROUND = set(['underground'])
RIVER = set(['river'])
ANY_TRANSIT = TAXI | BUS | UNDERGROUND | RIVER

ANY_LOCATION = FullBoard.keys()

ANY_START_LOCATION = [13, 26, 29, 34, 50, 53, 91, 94, 103, 112, 117, 132, 138,
    141, 155, 174, 197, 198]

Shorthand = {'taxi': 'T', 'bus': 'B', 'underground': 'U', 'river': 'R'}

def EmptyPath(start):
  return Path(start, [])

class Path:
  def __init__(self, start, transitions):
    self.start = start
    self.transitions = transitions

  def __str__(self):
    # ALTERNATE: return str((self.start, self.transitions))
    result = str(self.start)
    for t in self.transitions:
      result += " -" + Shorthand[t[0]] + "-> " + str(t[1])
    return result

  def finalLocation(self):
    if len(self.transitions) == 0:
      return self.start
    return self.transitions[-1][1]  # return destination of final step

  def copyWithPrefix(self, newStart, newTransit):
    oldStart = self.start
    return Path(newStart, [(newTransit, oldStart)] + self.transitions)

def PossiblePaths(starts, transits):
  if len(starts) == 0:
    return []  # no possible paths
  if len(starts) > 1:
    pathsFromFirstStart = PossiblePaths([starts[0]], transits)
    pathsFromOtherStarts = PossiblePaths(starts[1:], transits)
    return pathsFromFirstStart + pathsFromOtherStarts

  # If we reach this point, there is exactly one starting location.
  start = starts[0]

  if len(transits) == 0:
    return [EmptyPath(start)]  # one possible path of length zero

  paths = []
  currentTransitOptions = transits[0]
  remainingTransitOptions = transits[1:]
  for transit in currentTransitOptions:
    nextStarts = FullBoard[start][transit] \
        if transit in FullBoard[start] else []
    for nextStart in nextStarts:
      nextPaths = PossiblePaths([nextStart], remainingTransitOptions)
      for p in nextPaths:
        paths.append(p.copyWithPrefix(start, transit))
  return paths

def PossibleDestinations(starts, transits):
  paths = PossiblePaths(starts, transits)
  destinations = set()
  for p in paths:
    destinations.add(p.finalLocation())
  return sorted(list(destinations))

## Example
#starts = ANY_START_LOCATION
#transits = [TAXI, ANY_TRANSIT]
#paths = PossiblePaths(starts, transits)
#for path in paths:
#  print path
#print PossibleDestinations(starts, transits)

### SERVER ###

import urlparse
import BaseHTTPServer
import json

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):
    path = self.path
    if self.path == "/ScotlandYard.html":
      self.send_response(200)
      self.send_header("Content-type", "text/html")
      self.end_headers()
      f = open("ScotlandYard.html")
      self.wfile.write(f.read())
      f.close()
      return

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()

    if "?" in path:
      pathSplit = path.split("?", 1)
      params = urlparse.parse_qs(pathSplit[1])
    else:
      params = {}

    response = {"paths": [], "locations": []}

    if "starts" in params:
      starts = params["starts"][0]
      if starts == 'any':
        starts = ANY_LOCATION
      elif starts == 'any_start_location':
        starts = ANY_START_LOCATION
      else:
        starts = [int(n) for n in starts.split(",")]
      def parseTransit(s):
        if s == "taxi": return TAXI
        elif s == "bus": return BUS
        elif s == "underground": return UNDERGROUND
        elif s == "any": return ANY_TRANSIT
      if "transits" not in params:
        transits = []
      else:
        transits = map(parseTransit, params["transits"][0].split(","))

      paths = PossiblePaths(starts, transits)
      for path in paths:
        pathAsDict = {"start": path.start, "transitions": []}
        for step in path.transitions:
          pathAsDict["transitions"].append({"via": step[0], "to": step[1]})
        response["paths"].append(pathAsDict)
      response["locations"] = PossibleDestinations(starts, transits)

    self.wfile.write(json.dumps(response, sort_keys=True))

PORT = 8000

MyHandler.protocol_version = "HTTP/1.0"

server_address = ("127.0.0.1", PORT)
httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)

try:
  sa = httpd.socket.getsockname()
  print "Serving HTTP on", sa[0], "at port", sa[1]
  httpd.serve_forever()
except KeyboardInterrupt:
  print ""
  print "Shutting down web server"
  httpd.socket.close()
