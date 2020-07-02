from flask import Blueprint
from flask_restx import Api
from .train import api as train_ns
from .inference import api as inference_ns
from .status import api as status_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    title="Katana ML API Serving 🌻",
    version="0.5",
    description="A production ready model deployment template",
)

api.add_namespace(train_ns)
api.add_namespace(inference_ns)
api.add_namespace(status_ns)
