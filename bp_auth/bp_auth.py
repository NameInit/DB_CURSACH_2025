from flask import render_template, request, redirect, url_for, session
from model.model_route import model_route
from database.DBoperation import select, insert
from . import bp_auth, provider, cleaner


@bp_auth.route('/', methods=['GET', 'POST'])
def auth_handler():
    if request.method == 'GET':
        return render_template('auth.html')

    login = cleaner(request.form.get('login', ''))
    password = cleaner(request.form.get('password', ''))
    is_register = request.form.get('register') == 'true'

    if not login or not password:
        return render_template('auth.html', error="Введите логин и пароль")

    res = model_route(provider,
                      [login] if is_register else [login,password],
                      'get_user_by_name' 
                      if is_register else 
                      'get_user_role_by_name_passwd',select)

    if is_register and res.status:
        return render_template('auth.html', error="Логин занят")
    
    if not is_register and not res.status:
        return render_template('auth.html', error="Неверный логин или пароль")

    if is_register:
        model_route(provider,[login,password,4],'add_new_user',operator=insert)
        res = model_route(provider,[login,password],'get_user_role_by_name_passwd',select)

    session['id']=res.result[0][0]
    session['r_id']=res.result[0][3]
    session['user_group']=res.result[0][4]
    session['db_config']=res.result[0][5]

    return redirect(url_for('main_menu_handler'))

@bp_auth.route('/exit', methods=['GET'])
def exit_handler():
    return render_template('exit.html')