from flask import Flask
import os, json
from bp_query.bp_query import bp_query
from bp_auth.bp_auth import bp_auth
from bp_report.bp_report import bp_report
from bp_basket.bp_basket import bp_basket


base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
		static_folder=os.path.join(base_dir, 'static'),
		template_folder=os.path.join(base_dir, 'templates'))

app.secret_key="my key"
with open("./.config/db_config.json") as f:
	app.config['db_config']=json.load(f)
with open("./.config/bp_access.json") as f:
	app.config['bp_access']=json.load(f)
with open("./.config/cache_config.json") as f:
	app.config['cache_config']=json.load(f)

app.register_blueprint(bp_query, url_prefix='/query')
app.register_blueprint(bp_auth, url_prefix='/auth')
app.register_blueprint(bp_report, url_prefix='/report')
app.register_blueprint(bp_basket, url_prefix='/basket')