from flask import request
from flask_restx import Namespace, Resource, fields

api = Namespace("status", description="Namespace for utils")


@api.route("/isalive")
class IsAlive(Resource):
    def get(self):
        return {"success": "The API is up and running",
                "remote_ip_address" : str(request.remote_addr)}
