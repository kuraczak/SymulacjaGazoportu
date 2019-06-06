import pandas as pd
import numpy as np
# from pkg.Points import *
import Points

def pkt2robotMatrix(csvmap, n):
    # divides csv generated matrix into n slices for n robots
    checkpointList = []
    chargeList = []
    robotList = []
    checkpointIndex = 0
    chargeIndex = 0
    data = pd.read_csv(csvmap)
    rowIndex = 0
    matrix = data.values
    for r in matrix:
        for c in r:
            row = list(r)
            if c == 8:
                obj = Checkpoint(checkpointIndex, row.index(c), rowIndex)
                checkpointList.append(obj)
                checkpointIndex = checkpointIndex + 1
            if c == 7:
                new = Chargepoint(chargeIndex, row.index(c), rowIndex)
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
            distance = evaluatedistance(startPoint, chargepoint)
            distList.append(distance)
        distList = sorted(distList, key=lambda x: x[:][2])
        tmpPoint = distList[0][1]
        startPoint.chargePoint = Chargepoint(tmpPoint.index, tmpPoint.x, tmpPoint.y)
        distList.clear()

    iterator = 0
    for k in splitArray:
        robotList.append(robotData(iterator, list(k), k[0], k[centerIndex].chargePoint))
        iterator = iterator + 1
    return robotList
