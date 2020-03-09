import logging
from flask import Flask
from flask_restplus import Resource, Api
from waitress import serve
from flask import current_app as app


logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)
api = Api(app, version='1.0', title='Katana ML API', description='A boiler plate production level model deployement',)
logging.basicConfig(filename='./logs/katana.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

# Namespaces
ns_train = api.namespace('training', description='Training operations')
ns_infer = api.namespace('inference', description='Inference operations')
ns_info = api.namespace('info', description='API information')

@ns_info.route('/train')
class IsAlive(Resource):
    def get(self):
        return {'success': 'I am very much up :)'}

@ns_train.route('/predict')
class Training(Resource):
    def get(self):
        return {'success': 'Training pipeline'}

@ns_infer.route('/isalive')
class Inference(Resource):
    def get(self):
        return {'success': 'Inference pipeline'}

serve(app, host="0.0.0.0", port=8080)