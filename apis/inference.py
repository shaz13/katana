import pickle
import pandas as pd
from flask_restx import Namespace, Resource, fields
from flask import request
from configurations.config import MODEL_ROOT, TEMP_CSV

api = Namespace("inference", description="Namespace for inference")

personModel = api.model(
    "PersonDiabetes",
    {
        "Pregnancies": fields.String(required=True, example="2"),
        "Glucose": fields.String(required=True, example="109"),
        "BloodPressure": fields.String(required=True, example="92"),
        "SkinThickness": fields.String(required=True, example="1"),
        "Insulin": fields.String(required=True, example="1"),
        "BMI": fields.String(required=True, example="42.7"),
        "DiabetesPedigreeFunction": fields.String(required=True, example="0.85"),
        "Age": fields.String(required=True, example="54"),
    },
)


@api.route("/UCIDiabetes")
@api.doc(personModel)
@api.expect(personModel)
class Inference(Resource):
    def post(self):
        data = request.json
        prediction = self.predict(data)
        return {"success": "Prediction successful", "probability": str(prediction)}, 200

    def predict(self, data):
        # load the model from disk
        model = pickle.load(open(MODEL_ROOT, "rb"))
        print(data)
        instance = pd.DataFrame(data, index=[0])
        probability = round(model.predict_proba(instance)[:, 1][0], 4)
        return probability
