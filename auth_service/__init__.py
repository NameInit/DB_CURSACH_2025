from flask import Flask
from model.model_route import SQLProvider
import json, os

service_auth = Flask(__name__)

with open('./.config/db_config.json') as f:
    service_auth.config['db_config']=json.loads(f.read())

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'query'))