from flask import render_template, request, redirect, url_for, session
from model.model_route import model_route
from database.DBoperation import select, insert
from validators.str import cleaner
import requests
from . import bp_auth, provider


@bp_auth.route('/', methods=['GET', 'POST'])
def auth_handler():
    if request.method == 'GET':
        return render_template('auth.html')

    operation = "register" if request.form.get('register', False) else "login"
    type_user = "external" if request.form.get('external', False) else "internal"
    url = f"http://127.0.0.1:5001/api/{type_user}/{operation}"
    data_dict = {
        'login': request.form.get('login', ''), 
        'password': request.form.get('password', '')
    }

    response=requests.post(url, json=data_dict)

    if not response.json().get('success', False):
        return render_template('auth.html', error=response.json().get('err_message', "Unkwon Error"))

    session['id']=response.json()['data'].get('id', None)
    session['r_id']=response.json()['data'].get('r_id', None)
    session['user_group']=response.json()['data'].get('user_group', None)
    session['db_config']=response.json()['data'].get('db_config', None)
    return redirect(url_for('main_menu_handler'))

@bp_auth.route('/exit', methods=['GET'])
def exit_handler():
    return render_template('exit.html')