from flask_restplus import Namespace, Resource, fields

api = Namespace('utils', description='Namespace for utils')

@api.route('/isalive')
class IsAlive(Resource):
    def get(self):
        app.logger.info("Pinging API alive status")
        return {'success': 'I am up and running :)'}