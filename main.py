import yaml
import logging
import os

from flask import Flask
from flask_restplus import Resource, Api
from apis import api

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')
api.init_app(app)

if __name__ == '__main__':

    if not os.path.exists("./core/models"):
        os.makedirs("./core/models", exist_ok=True)
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])
