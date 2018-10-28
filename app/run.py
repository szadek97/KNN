from app.classes.dataOperations import dataOperations
from app.classes.kNN import kNN

data = dataOperations();
irisLearningData = data.loadData('./data-sources/iris.data.learning')
irisTestData = data.loadData('./data-sources/iris.data.test')
irisTestDataWithoutLabels = data.removeLabels(irisTestData)

kNN = kNN(3, irisLearningData)
unsetLabelsList = kNN.predict(irisTestDataWithoutLabels)

print("Score: ",kNN.score(irisTestData, unsetLabelsList))
print("Accuracy: ",(kNN.score(irisTestData, unsetLabelsList)))
