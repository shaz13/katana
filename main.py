import yaml
import logging
import os
import logging.config

from flask import Flask, render_template
from apis import api

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)
api.init_app(app)

logging.config.fileConfig('gunicorn_logging.conf')

if __name__ == '__main__':

    if not os.path.exists("./core/models"):
        os.makedirs("./core/models", exist_ok=True)
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])
