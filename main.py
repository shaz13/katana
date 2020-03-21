import yaml
import logging

from flask import Flask
from flask_restplus import Resource, Api
from waitress import serve
from flask import current_app as app

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


app = Flask(__name__)
api = Api(app, version='0.1', title='Katana ML API', description='A boiler plate production level model deployement',)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')

# Namespaces
ns_train = api.namespace('training', description='Training operations')
ns_infer = api.namespace('inference', description='Inference operations')
ns_info = api.namespace('info', description='API information')

@ns_info.route('/isalive')
class IsAlive(Resource):
    def get(self):
        return {'success': 'I am very much up :)'}

@ns_train.route('/train')
class Training(Resource):
    def get(self):
        app.logger.info("Received index load")
        return {'success': 'Training pipeline'}

@ns_infer.route('/predict')
class Inference(Resource):
    def get(self):
        return {'success': 'Inference pipeline'}

if __name__ == '__main__':
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])