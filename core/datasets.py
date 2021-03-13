from sklearn import datasets


class IrisDatasetLoader:
    def __init__(self):
        self.data = datasets.load_iris()

    def load_data(self):
        X = self.data.data
        y = self.data.target
        return X, y


if __name__ == "__main__":
    dataset_loader = IrisDatasetLoader()
    print(dataset_loader.load_data())
