from flask import render_template, request, redirect, url_for
from validators.decorator import group_required
from . import bp_query, provider, forms
from model.model_route import model_route
from database.DBoperation import select


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