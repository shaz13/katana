import yaml
import os
import logging.config
import yaml

from flask import Flask
from apis import api
from colored_logging import ColorFormatter

with open(r'config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)
api.init_app(app)

# create logger
logging.ColorFormatter = ColorFormatter
logging.config.fileConfig('gunicorn_logging.conf')

if __name__ == '__main__':

    if not os.path.exists("./core/models"):
        os.makedirs("./core/models", exist_ok=True)
    app.logger.info("Starting the ML Engines")
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])
