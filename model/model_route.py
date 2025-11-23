from dataclasses import dataclass
from database.SQLprovider import SQLProvider
from database import DBoperation

@dataclass
class ResultInfo:
	result: tuple
	status: bool
	err_message: str

def model_route(provider: SQLProvider, params: list, operation:str, operator:DBoperation)->ResultInfo:
	query=provider.get(operation+'.sql') if not isinstance(operation,list) else list(map(lambda x: provider.get(x+'.sql'), operation))
	res=operator(query,params)
	return ResultInfo(res, True, '') if res else ResultInfo(res, False, 'Ошибка запроса')	