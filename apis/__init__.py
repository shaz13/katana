from flask_restplus import Api
from .train import api as train_ns
from .inference import api as inference_ns
from .utils import api as utils_ns

api = Api(
    title='Katana API',
    version='0.2',
    description='A boilerplate production ML API',
)

api.add_namespace(train_ns)
api.add_namespace(inference_ns)
api.add_namespace(utils_ns)
