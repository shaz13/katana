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
            X, y = self.data.load_data()
            classifier.fit(X, y)
        except Exception as e:
            raise (e)
        return classifier
