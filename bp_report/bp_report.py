from . import bp_report


@bp_report.route('/')
def report_menu_handler():
	return "Menu report"
