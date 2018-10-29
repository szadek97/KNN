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
        for item in dataArray:
            dataArrayWithoutLabels.append(item[0:len(item)-1])
        return np.array(dataArrayWithoutLabels)
        dataArrayWithoutLabels = np.array(dataArrayWithoutLabels)
        return dataArrayWithoutLabels

    def getLabels(self, array):
        newArr = []
        for item in array:
            newArr.append(item[len(item) - 1])
        return np.array(newArr)
