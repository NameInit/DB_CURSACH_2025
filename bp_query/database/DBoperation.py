from .DBcm import DBContextManager
from flask import current_app


def select(sql:str, param_list:list=[])->list[tuple]:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			return cursor.fetchall()