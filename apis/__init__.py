from flask_restx import Api
from .train import api as train_ns
from .inference import api as inference_ns
from .utils import api as utils_ns

api = Api(
    title='Katana ML API Serving 🌻',
    version='0.5',
    description='A production ready model deployment template',
)

api.add_namespace(train_ns)
api.add_namespace(inference_ns)
api.add_namespace(utils_ns)
