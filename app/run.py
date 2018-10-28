from app.classes.dataOperations import dataOperations

data = dataOperations();
irisLearningData = data.loadData('./data-sources/iris.data.learning')
irisTestData = data.loadData('./data-sources/iris.data.test')
