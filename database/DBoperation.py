from .DBcm import DBContextManager
from flask import current_app, session
from . import message_to_bool


def select(sql:str, param_list:list=[])->list[tuple]:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			return cursor.fetchall()

def insert(sql:str, param_list:list=[])->bool:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			return True
		
def call(sql:str, param_list:list=[]):
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			return message_to_bool(cursor.connection.notices[0].strip(), 'SUCCESS')