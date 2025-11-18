from flask import render_template, request
from model.model_route import model_route
from database.DBoperation import select,insert,call
from validators.decorator import group_required
from . import bp_report, provider


@bp_report.route('/', methods=['GET'])
@group_required
def report_menu_handler():
    return render_template("report_menu.html")

@bp_report.route('/<int:report_id>/<action>')
@group_required
def report_form_handler(report_id, action):
    return render_template("report_input_form.html", report_id=report_id, action=action)

@bp_report.route('/create', methods=['POST'])
@group_required
def report_create_handler():
    params = list(request.form.values())
    report_id = int(params.pop())    
    res = model_route(provider, params, 'report' + str(report_id), call)
    return render_template("report_message.html", success=res.status)

@bp_report.route('/view', methods=['POST'])
@group_required
def report_view_handler():
    params = list(request.form.values())
    report_id = int(params.pop())
    res = model_route(provider, params, 'get_report', select)
    return render_template("report_results.html", 
                            report_id=report_id, 
                            title=['report_id','p_month','p_year','p_amount','p_value'], 
                            result=res.result)