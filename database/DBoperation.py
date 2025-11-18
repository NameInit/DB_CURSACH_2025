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
			return cursor.fetchone()[0] if cursor.description else True #аналог cursor.lastrowid
		
def call(sql:str, param_list:list=[]) -> bool:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			return message_to_bool(cursor.connection.notices[0].strip(), 'SUCCESS')
		
def select_dict(sql:str, param_list:list=[]) -> list[dict]:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.execute(sql, param_list)
			col_names=[item[0] for item in cursor.description]
			results = []
			for row in cursor.fetchall():
				row_dict = {}
				for i, col_name in enumerate(col_names):
					row_dict[col_name] = row[i]
				results.append(row_dict)

			return results

def tranzakt(list_sql:list[str], list_param_list:list[list]=[])->bool:
	with DBContextManager(current_app.config['db_config']) as cursor:
		if cursor is None:
			raise ValueError('Не могу подключиться к базе данных')
		else:
			cursor.connection.autocommit=False
			for i in range(len(list_sql)):
				cursor.execute(list_sql[i], list_param_list[i])
			return True