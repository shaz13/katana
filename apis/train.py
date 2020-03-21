from flask_restplus import Namespace, Resource, fields

api = Namespace('train', description='Namespace for training')

@api.route('/fit')
class Train(Resource):
    def get(self):
        return {'success': 'Training pipeline successful'}