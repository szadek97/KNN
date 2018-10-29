import unittest
from app.classes.dataOperations import dataOperations
from app.classes.kNN import kNN

data = dataOperations()
irisLearningData = data.loadData('./data-sources/iris.data.learning')
irisTestData = data.loadData('./data-sources/iris.data.test')

class test_kNN(unittest.TestCase):

    def test_score(self):
        unsetLabels = data.getLabels(irisTestData)
        expected = 13
        test = kNN(3,irisLearningData)
        result = test.score(irisTestData,unsetLabels)
        self.assertEqual(expected, result)

if __name__ == '_main_':
    unittest.main()