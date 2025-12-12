from flask import jsonify, request
from .validators.str import cleaner
from .model.model_route import model_route
from .database.DBoperation import select, insert
from . import service_auth, provider

@service_auth.route('/api/health', methods=['GET'])
def check():
	print("Hello! It is REST-API Auth!")
	return jsonify({'success': True, 'error': None}), 200

@service_auth.route('/api/external/login', methods=['POST'])
def external_login():
	login=cleaner(request.json['login'])
	password=cleaner(request.json['password'])
	db_config = service_auth.config['db_config']
	res=model_route(provider, [login, password], 'eget_user_by_name_passwd', select, db_config)
	data=dict()
	if res.status:
		data={
			'id': res.result[0][0],
			'user_group': service_auth.config['external']['user_group'],
			'db_config': service_auth.config['external']['db_config']
		}
	return jsonify({
		'success': res.status, 
		'err_message': "" if res.status else "Неверный логин или пароль", 
		'data': data}), 200 if res.status else 401

@service_auth.route('/api/external/register', methods=['POST'])
def external_register():
	login=cleaner(request.json['login'])
	password=cleaner(request.json['password'])
	db_config = service_auth.config['db_config']
	res=model_route(provider, [login], 'eget_user_by_name', select, db_config)

	if res.status:
		return jsonify({'success': False, 'err_message': "Логин занят", 'data': {}}), 401
	
	model_route(provider, [login,password], 'eadd_new_user', insert, db_config)
	res=model_route(provider, [login,password], 'eget_user_by_name_passwd', select, db_config)

	data=dict()
	if res.status:
		data={
			'id': res.result[0][0],
			'user_group': service_auth.config['external']['user_group'],
			'db_config': service_auth.config['external']['db_config']
		}

	return jsonify({
		'success': res.status,
		'err_message': "" if res.status else "Не могу зарегестрировать", 
		'data': data}), 200 if res.status else 401

@service_auth.route('/api/internal/login', methods=['POST'])
def internal_login():
	login=cleaner(request.json['login'])
	password=cleaner(request.json['password'])
	db_config = service_auth.config['db_config']
	res=model_route(provider, [login, password], 'iget_user_role_by_name_passwd', select, db_config)
	data=dict()
	if res.status:
		data={
			'id': res.result[0][0],
			'user_group': res.result[0][4],
			'db_config': res.result[0][5]
		}

	return jsonify({
		'success': res.status, 
		'err_message': "" if res.status else "Неверный логин или пароль", 
		'data': data}), 200 if res.status else 401

@service_auth.route('/api/internal/register', methods=['POST'])
def internal_register():
	login=cleaner(request.json['login'])
	password=cleaner(request.json['password'])
	db_config = service_auth.config['db_config']
	res = model_route(provider, [login], 'iget_user_by_name', select, db_config)

	if res.status:
		return jsonify({'success': False, 'err_message': "Логин занят", 'data': {}}), 401
	data=dict()
	model_route(provider,[login,password,4],'iadd_new_user', insert, db_config)
	res = model_route(provider,[login,password],'iget_user_role_by_name_passwd', select, db_config)
	data={
		'id': res.result[0][0],
		'user_group': res.result[0][4],
		'db_config': res.result[0][5]
	}
	return jsonify({
		'success': True, 
		'err_message': "", 
		'data': data}), 200