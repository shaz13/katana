from loguru import logger
from core.datasets import IrisDatasetLoader
from sklearn import svm


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
