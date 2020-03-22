import pickle
import pandas as pd
from flask_restplus import Namespace, Resource, fields
from flask import request
from apis.config import MODEL_ROOT

api = Namespace('inference', description='Namespace for inference')

personModel = api.model('PersonDiabetes', {
    'Pregnancies': fields.String(required=True),
    'Glucose': fields.String(required=True),
    'BloodPressure': fields.String(required=True),
    'SkinThickness': fields.String(required=True),
    'Insulin': fields.String(required=True),
    'BMI': fields.String(required=True),
    'DiabetesPedigreeFunction': fields.String(required=True),
    'Age': fields.String(required=True),
})


@api.route('/UCIDiabetes')
@api.doc(personModel)
@api.expect(personModel)
class Inference(Resource):
    def post(self):
        data = request.json
        prediction = self.predict(data)
        return {'success': 'Prediction successful',
                'probability': str(prediction)
                }, 200

    def predict(self, data):
        # load the model from disk
        model = pickle.load(open(MODEL_ROOT, 'rb'))
        print(data)
        instance = pd.DataFrame(data, index=[0])
        probability = round(model.predict_proba(instance)[:, 1][0], 4)
        return probability
