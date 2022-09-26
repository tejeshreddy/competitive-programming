from enum import Enum
from heapq import heappush, heappop

class Direction(Enum):
    up = 'UP'
    down = 'DOWN'
    idle = 'IDLE'

class RequestType(Enum):
    external = 'EXTERNAL'
    internal = 'INTERNAL'

class Request:
    def __init__(self, origin, target, typeR, direction):
        self.origin = origin
        self.target = target
        self.typeRequest: RequestType = typeR
        self.direction = direction

class Button:
    def __init__(self, floor):
        self.floor = floor

class Elevator:
    def __init__(self, currectFloor):
        self.direction = Direction.idle
        self.currentFloor = currectFloor
        self.upStops = []
        self.downStops = []
    
    def sendUpRequest(self, upRequest):
        if upRequest.typeRequest == RequestType.external:
            heappush(self.upStops, (upRequest.origin, upRequest.origin))
        
        heappush(self.upStops, (upRequest.target, upRequest.origin))
    
    def sendDownRequest(self, downRequest):
        if downRequest.typeRequest == RequestType.external:
            heappush(self.downStops, (-downRequest.origin, downRequest.origin))
        
        heappush(self.downStops, (-downRequest.target, downRequest.origin))
    
    def processRequests(self):
        if self.direction in [Direction.up, Direction.idle]:
            self.processUpRequests()
            self.processDownRequests()
        else:
            self.processDownRequests()
            self.processUpRequests()

    def processUpRequests(self):
        while self.upStops:
            target, origin = heappop(self.upStops)
            self.currentFloor = target
            if abs(target) == origin:
                print("Picking up people")
            else:
                print("Stopping to pick up")

        if self.downStops:
            self.direction = Direction.down
        else:
            self.direction = Direction.idle
    
    def processDownRequests(self):
        while self.downStops:
            target, origin = heappop(self.downStops)
            self.currentFloor = target
            if abs(target) == origin:
                print("Picking up")
            else:
                print("Dropping off")
        if self.upStops:
            self.direction = Direction.up
        else:
            self.direction = Direction.idle



