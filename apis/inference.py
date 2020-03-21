from flask_restplus import Namespace, Resource, fields

api = Namespace('inference', description='Namespace for inference')

@api.route('/predict')
class Inference(Resource):
    def get(self):
        app.logger.info("Predicting results")
        return {'success': 'Prediction successful'}