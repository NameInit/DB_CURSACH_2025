from flask import render_template, session, redirect, url_for
from model.model_route import model_route
from . import app

def login_required(func):
	from functools import wraps
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'user_group' in session:
			return func(*args, **kwargs)
		else:
			return redirect(url_for('bp_auth.auth_handler'))
	return wrapper

@app.route('/', methods=['GET'])
@login_required
def main_menu_handler():
	return render_template('main_menu.html')

@app.route('/exit', methods=['GET'])
@login_required
def exit_handler():
	session.clear()
	return redirect(url_for('bp_auth.auth_handler'))