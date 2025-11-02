from flask import redirect, url_for, session, current_app, request

def login_required(func):
	from functools import wraps
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'user_group' in session:
			return func(*args, **kwargs)
		else:
			return redirect(url_for('bp_auth.auth_handler'))
	return wrapper

def group_required(func):
	from functools import wraps
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'user_group' in session:
			access = current_app.config['db_access']
			user_request = request.endpoint.split('.')[0]
			user_role=session.get('user_group')
			if user_role in access and user_request in access[user_role]:
				return func(*args, **kwargs)
			else:
				return "Permission denied"
		return "Need to auth"
	return wrapper