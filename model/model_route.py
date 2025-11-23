from dataclasses import dataclass
from database.SQLprovider import SQLProvider
from database import DBoperation

@dataclass
class ResultInfo:
	result: tuple
	status: bool
	err_message: str

def model_route(provider: SQLProvider, params: list, operation:str, operator:DBoperation, db_config: dict)->ResultInfo:
	query=provider.get(operation+'.sql') if not isinstance(operation,list) else list(map(lambda x: provider.get(x+'.sql'), operation))
	res=operator(query,params,db_config)
	return ResultInfo(res, True, '') if res else ResultInfo(res, False, 'Ошибка запроса')	