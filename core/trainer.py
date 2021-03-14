from loguru import logger
from core.datasets import IrisDatasetLoader, BostonDatasetLoader
from sklearn import svm
from sklearn.linear_model import LinearRegression


class IrisTrainerInstance:
    def __init__(self):
        pass

    def load_data(self):
        self.data = IrisDatasetLoader()

    def train(self):
        try:
            classifier = svm.SVC()
            logger.info("Fetching dataset")
            X, y = self.data.load_data()
            logger.info("Training SVC Model")
            classifier.fit(X, y)
        except Exception as e:
            raise (e)
        return classifier


class BostonHousePriceTrainerInstance:
    def __init__(self):
        self.dataloder = BostonDatasetLoader()

    def train(self):
        self.X, self.y = self.dataloder.load_data()
        model = LinearRegression()
        model.fit(self.X, self.y)
        return model
