from flask import Flask, render_template, session, redirect, url_for
from bp_query.bp_query import bp_query
from bp_auth.bp_auth import bp_auth
import json, os

def login_required(func):
	from functools import wraps
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'user_group' in session:
			return func(*args, **kwargs)
		else:
			return redirect(url_for('bp_auth.auth_handler'))
	return wrapper

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
           static_folder=os.path.join(base_dir, 'static'),
           template_folder=os.path.join(base_dir, 'templates'))

app.secret_key="my key"
with open("./.config/db_config.json") as f:
	app.config['db_config']=json.load(f)
with open("./.config/db_access.json") as f:
	app.config['db_access']=json.load(f)

app.register_blueprint(bp_query, url_prefix='/query')
app.register_blueprint(bp_auth, url_prefix='/auth')

@app.route('/', methods=['GET'])
@login_required
def main_menu_handler():
	return render_template('main_menu.html')

@app.route('/exit', methods=['GET'])
@login_required
def exit_handler():
	session.clear()
	return redirect(url_for('bp_auth.auth_handler'))

if __name__=='__main__':
	app.run(host="127.0.0.1", port=5000, debug=True)