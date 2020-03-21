from flask_restplus import Api

from .train import api as train_ns
from .inference import api as inference_ns
from .utils import api as utils_ns

api = Api(
    title='Katana ML API',
    version='0.1',
    description='A boiler plate production level model deployement',
)

api.add_namespace(train_ns)
api.add_namespace(inference_ns)
api.add_namespace(utils_ns)