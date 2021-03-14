from sklearn import datasets


class IrisDatasetLoader:
    def __init__(self):
        self.data = datasets.load_iris()

    def load_data(self):
        X = self.data.data
        y = self.data.target
        return X, y


class BostonDatasetLoader:
    def __init__(self):
        self.X = None
        self.y = None

    def load_data(self):
        self.X, self.y = datasets.load_boston(return_X_y=True)
        return self.X, self.y
