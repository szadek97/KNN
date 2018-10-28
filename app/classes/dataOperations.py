import numpy as np
import pandas as pd

class dataOperations:
    def __init__(self):
        return None

    def loadData(self, path):
        loadedData = pd.read_csv(path)
        dataArray = np.array(loadedData)
        return dataArray

    def removeLabels(self, dataArray):
        dataArrayWithoutLabels = []
        for x in range(len(dataArray)):
            dataArrayWithoutLabels.append(x[len(x) - 1])
        dataArrayWithoutLabels = np.array(dataArrayWithoutLabels)
        return dataArrayWithoutLabels
