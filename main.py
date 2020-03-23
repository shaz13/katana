import os
import yaml
import logging
import logging.config

from flask import Flask
from apis import api
from apis.config import ColorFormatter

with open(r'./configurations/config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

app = Flask(__name__)
api.init_app(app)

logging.ColorFormatter = ColorFormatter
print(config['LOGGING_CONFIG'])
logging.config.fileConfig(config['LOGGING_CONFIG'])

if __name__ == '__main__':

    if not os.path.exists(config['MODEL_DIR']):
        os.makedirs(config['MODEL_DIR'], exist_ok=True)
    app.run(debug=config['DEBUG'], host=config['HOST'], port=config['PORT'])
