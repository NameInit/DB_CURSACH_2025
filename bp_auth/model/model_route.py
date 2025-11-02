from dataclasses import dataclass
from ..database.SQLprovider import SQLProvider
from ..database.DBoperation import select


@dataclass
class ResultInfo:
	result: tuple
	status: bool
	err_message: str

def model_route(provider: SQLProvider, params: list, index_query:int)->ResultInfo:
	query=provider.get("query"+str(index_query)+".sql")
	res=select(query,params)
	return ResultInfo(res, True, '') if res else ResultInfo(res, False, 'Не найдены данные')
	