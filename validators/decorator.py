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
			bp_name,handler_name=request.endpoint.split('.')
			access=current_app.config['bp_access']
			user_role=session.get('user_group')
			# print(user_role,access,user_role in access,sep='\n')
			if user_role in access and bp_name in access[user_role] and (handler_name in access[user_role][bp_name] or access[user_role][bp_name]=='*'):
				return func(*args, **kwargs)
			else:
				return "Permission denied"
		return "Need to auth"
	return wrapper