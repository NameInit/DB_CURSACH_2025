from dataclasses import dataclass
from database.SQLprovider import SQLProvider


@dataclass
class ResultInfo:
	result: tuple
	status: bool
	err_message: str

def model_route(provider: SQLProvider, params: list, operation:str, operator)->ResultInfo:
	query=provider.get(operation+'.sql')
	res=operator(query,params)
	return ResultInfo(res, True, '') if res else ResultInfo(res, False, 'Ошибка запроса')