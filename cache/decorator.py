from flask import current_app
from .RedisCache import RedisCache
from model.model_route import ResultInfo


def redis_cache(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        redis=RedisCache(current_app.config['cache_config'])
        name=func.__name__+":"+":".join(str(arg) for arg in args)+":" + ":".join(f"{k}:{v}" for k, v in kwargs.items())
        result=redis.get_value(name)
        if result:
            return ResultInfo(**result)
        response = func(*args,**kwargs)
        redis.set_value(name,response.__dict__)
        return response
    return wrapper