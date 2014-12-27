#!/usr/bin/python

import StandardBoard


FullBoard = StandardBoard.FullBoard

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

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def writeLines(self, *lines):
    for line in lines:
      self.wfile.write(line + "\n")

  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    path = self.path
    if "?" in path:
      params = urlparse.parse_qs(path.split("?", 1)[1])
    else:
      params = {}

    self.writeLines(
        "<html>",
        "<body>",
        "Params = " + str(params),
        "<br/>")

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
      self.writeLines(
          "Starts = " + str(starts),
          "<br/>",
          "Transits = " + str(transits),
          "<br/>")
      result = PossiblePaths(starts, transits)
      for path in result:
        self.writeLines(str(path),
            "<br/>")
      result = PossibleDestinations(starts, transits)
      self.writeLines("Destinations: " + str(result))

    self.writeLines(
        "<img src=\"http://worldofstuart.excellentcontent.com/unlocked/scotland/scotyardfull.jpg\"/>",
        "</body>",
        "</html>")

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
