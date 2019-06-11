import pandas as pd
import numpy as np
# from pkg.Points import *
import robot

def pkt2robotMatrix(data, n):
    # divides csv generated matrix into n slices for n robots
    checkpointList = []
    chargeList = []
    robotList = []
    checkpointIndex = 0
    chargeIndex = 0
    rowIndex = 0
    for r in data:
        for c in r:
            row = list(r)
            if c == 8:
                obj = robot.Checkpoint(checkpointIndex, row.index(c), rowIndex)
                checkpointList.append(obj)
                checkpointIndex = checkpointIndex + 1
            if c == 7:
                new = robot.Chargepoint(chargeIndex, row.index(c), rowIndex)
                chargeList.append(new)
                chargeIndex = chargeIndex + 1
        rowIndex = rowIndex + 1

    centerIndex= int(checkpointIndex/(n*2))
    checkpointList = sorted(checkpointList, key=lambda o: o.x)
    splitArray = np.array_split(checkpointList, n)
    for i in splitArray:
        distList = []
        startPoint = i[centerIndex]
        for chargepoint in chargeList:
            distance = robot.evaluatedistance(startPoint, chargepoint)
            distList.append(distance)
        distList = sorted(distList, key=lambda x: x[:][2])
        tmpPoint = distList[0][1]
        startPoint.chargePoint = robot.Chargepoint(tmpPoint.index, tmpPoint.x, tmpPoint.y)
        distList.clear()

    iterator = 0
    for k in splitArray:
        robotList.append(robot.Robot(1, 200, data, k[centerIndex].chargePoint, iterator, k[centerIndex].chargePoint)
        iterator = iterator + 1
    return robotList
