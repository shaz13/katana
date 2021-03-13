from core.datasets import IrisDatasetLoader
from sklearn.linear_model import LogisticRegression


class IrisTrainerInstance:
    def __init__(self):
        pass

    def load_data(self):
        self.data = IrisDatasetLoader()

    def train_linear_model(self):
        try:
            logreg = LogisticRegression(random_state=13)
            X, y = self.data.load_data()
            logreg.fit(X, y)
        except Exception as e:
            raise (e)
        return logreg
