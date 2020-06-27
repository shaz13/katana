from flask_restx import Namespace, Resource, fields
from core.training import TrainLogisticClassifier

api = Namespace("train", description="Namespace for training")


@api.route("/UCIDiabetes")
class TrainEndPoint(Resource):
    def __init__(self, model=None):
        self.model = None

    def load_model(self, model_instance):
        self.model = model_instance
        return self.model

    def post(self):
        model = self.load_model(TrainLogisticClassifier())
        training_info = model.train(target_var="Outcome")
        return training_info
