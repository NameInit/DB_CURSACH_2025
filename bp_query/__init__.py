from flask import Blueprint
from .database.SQLprovider import SQLProvider
import os

bp_query = Blueprint('bp_query', __name__, 
                    template_folder='./templates',
                    static_folder='./static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__),'query'))
param_form = {
    1: [1, 1, 0],
    2: [1, 1, 0],
    3: [1, 1, 1],
    4: [0, 0, 0],
    5: [1, 1, 0],
    6: [1, 0, 1]
}
titles = {
	1: ["ID", "MedicineName", "Count"],
    2: ["ID", "ProviderName", "Summa"],
    3: ["ID", "ProviderName", "City", "DateOpenDel", "DateCloseDel"],
    4: ["ID", "ProviderName", "City", "DateOpenDel", "DateCloseDel"],
    5: ["ID", "ProviderName", "City", "DateOpenDel", "DateCloseDel"],
    6: ["ID", "ProviderName", "City", "DateOpenDel", "DateCloseDel"]
}