from flask import Blueprint
from database.SQLprovider import SQLProvider
import os, json

bp_query = Blueprint('bp_query', __name__, 
                    template_folder='./templates',
                    static_folder='./static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__),'query'))

forms = json.load(open(f"./{__name__}/.config/forms.json",encoding='utf-8'))