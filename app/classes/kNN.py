import math
import scipy.spatial as sp
import operator

class kNN:
    def __init__(self, k, learningData):
        self.k = k
        self.learningData = learningData

    def predict(self, data):
        knownLabelsList = []
        for i in range(len(data)):
            distances = []
            for j in range(len(self.learningData)):
                distance = sp.distance.euclidean(self.learningData[j][0:3], data[i][0:3])
                distances.append((self.learningData[j], distance))
                distances.sort(key=operator.itemgetter(1))
            neighborsList = []
            for x in range(self.k):
                neighborsList.append(distances[x][0])
            knownLabelsList.append(getLabels(neighborsList))
        return knownLabelsList

    def score(self, testingData, labels):
        correct = 0
        for i in range(len(testingData)):
            data = testingData[i]
            if data[4] == labels[i]:
                correct += 1
        return (correct/len(testingData))*100

def getLabels(neighborsList):
    resultLabels = {}
    for i in range(len(neighborsList)):
        label = neighborsList[i][-1]
        if label in resultLabels:
            resultLabels[label] += 1
        else:
            resultLabels[label] = 1
    sortedLabels = sorted(resultLabels.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedLabels[0][0]
