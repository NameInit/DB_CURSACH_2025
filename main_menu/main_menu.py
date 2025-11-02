from flask import render_template, session, redirect, url_for
from validators.decorator import login_required
from . import app


@app.route('/', methods=['GET'])
@login_required
def main_menu_handler():
	return render_template('main_menu.html')

@app.route('/exit', methods=['GET'])
@login_required
def exit_handler():
	session.clear()
	return redirect(url_for('bp_auth.auth_handler'))