from flask import Blueprint
from database.SQLprovider import SQLProvider
import os

bp_auth = Blueprint('bp_auth', __name__, 
			template_folder='./templates',
			static_folder='./static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'query'))