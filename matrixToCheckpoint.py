import pandas as pd
import numpy as np
import Checkpoint

def matrixToCheckpoint(csv_file, n=1):
    checkpointList=[]
    index=0
    data = pd.read_csv(csv_file)
    matrix = data.values

    for r in matrix:
        newList = list(r)
        for c in r:
            if c == 7:
                obj = Checkpoint(index, newList.index(c), c)
                checkpointList.append(obj)
                index = index+1
    slicedList = np.array_split(checkpointList, n)
    return slicedList
