import os


class SQLProvider:
	def __init__(self, path: str):
		self.requests:dict=dict()
		for filename in os.listdir(path):
			request:str=open(f"{path}/{filename}").read()
			self.requests[filename]=request
	
	def get(self, filename: str) -> str:
		return self.requests[filename]