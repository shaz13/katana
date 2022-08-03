from transformers import pipeline


class MaskLanguageModelPipe:
    def __init__(self):
        self.task = "fill-mask"
        self.model_name = "distilbert-base-uncased"

    def predict(self, text):
        model = pipeline(self.task, model=self.model_name)
        return model(text)
