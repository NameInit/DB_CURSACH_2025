from flask import render_template, request, redirect, url_for, current_app, session
from . import bp_query, provider, forms
from model.model_route import model_route
from database.DBoperation import select


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

params_title = ('year', 'month', 'm_id')

@bp_query.route('/', methods=['GET'])
@group_required
def query_menu_handler():
    return render_template('query_menu.html')

@bp_query.route('/<int:query_id>', methods=['GET'])
@group_required
def query_form_handler(query_id):    
    if forms["param_form"][str(query_id)].count(0) == len(forms["param_form"][str(query_id)]):
        return redirect(url_for('bp_query.query_result_handler', query_id=query_id))
    return render_template("query_input_form.html", 
                         param_form=forms["param_form"][str(query_id)],
                         query_id=query_id)

@bp_query.route('/result', methods=['GET', 'POST'])
@group_required
def query_result_handler():
    params = list(request.form.values())
    query_id = int(request.args.get('query_id')) if request.args.get('query_id') is not None else int(params.pop())
    res=model_route(provider,params,'query'+str(query_id),select)
    return render_template("query_results.html", 
						   query_id=query_id, 
						   title=forms["titles"][str(query_id)], 
						   result=res.result)