from flask import render_template, request
from model.model_route import model_route
from database.DBoperation import select,insert,call
from validators.decorator import group_required
from . import bp_report, provider, forms


@bp_report.route('/', methods=['GET'])
@group_required
def report_menu_handler():
    return render_template("report_menu.html")

@bp_report.route('/<int:report_id>/create', methods=['GET'])
@group_required
def report_form_create_handler(report_id):
    fields = forms["param_form"][str(report_id)]
    return render_template("report_input_form.html", report_id=report_id, action="create", fields = fields)

@bp_report.route('/<int:report_id>/view', methods=['GET'])
@group_required
def report_form_view_handler(report_id):
    fields = forms["param_form"][str(report_id)]
    return render_template("report_input_form.html", report_id=report_id, action="view", fields = fields)

@bp_report.route('/<int:report_id>/<action>/result', methods=['POST'])
@group_required
def report_result_handler(report_id, action):
    params = list(request.form.values())
    params.pop()
    
    if action == 'create':
        res = model_route(provider, params, 'report' + str(report_id), call)
        return render_template("report_message.html", success=res.status)
    elif action == 'view':
        title = forms["res_title"][str(report_id)]
        res = model_route(provider, params, 'get_report', select)
        return render_template("report_results.html", 
                              report_id=report_id, 
                              title=title, 
                              result=res.result)
    return "Not found"