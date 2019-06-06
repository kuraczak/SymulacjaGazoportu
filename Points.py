import numpy as np


class Chargepoint:
    def __init__(self, index=0, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        self.index = index

    def __eq__(self, other):
        if other.x == self.x & other.y == self.y:
            return True
        else:
            return False

class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

class Checkpoint:
    def __init__(self, index=0, coord_x=0, coord_y=0, charge=Chargepoint()):
        self.index = index
        self.y = coord_y
        self.x = coord_x
        self.chargePoint = charge


def evaluatedistance(checkpoint, chargepoint):
    dist = np.sqrt((checkpoint.x - chargepoint.x) ** 2 + (checkpoint.y - chargepoint.y) ** 2)
    return [checkpoint, chargepoint, dist]


class robotData:
    def __init__(self, robotId=0, checkpoints=[], startPos=Point(), chargePoint=Chargepoint()):
        self.index = robotId
        self.checkpoints = checkpoints
        self.startPos = startPos
        self.chargePoint = chargePoint
