from flask import Blueprint
from database.SQLprovider import SQLProvider
import os

bp_auth = Blueprint('bp_auth', __name__, 
			template_folder='./templates',
			static_folder='./static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'query'))

def cleaner(s: str):
    import re
    return re.sub(r'[^a-zA-Z0-9_]', '', s)