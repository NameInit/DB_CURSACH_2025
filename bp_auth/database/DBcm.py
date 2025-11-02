from psycopg2.extensions import connection, cursor
from psycopg2 import OperationalError
from psycopg2 import connect


class DBContextManager:
	def __init__(self, db_connect: dict):
		self.conn:connection=None
		self.cursor:cursor=None
		self.db_connect=db_connect
	
	def __enter__(self):
		try:
			self.conn=connect(**self.db_connect)
			self.cursor=self.conn.cursor()
			return self.cursor
		except OperationalError as err:
			print(err.args)
			return None
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type:
			print(f"{exc_type=}")
			print(f"{exc_val=}")
		if self.cursor:
			self.conn.rollback() if exc_type else self.conn.commit()
			self.cursor.close()
			self.conn.close()