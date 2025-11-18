from redis import Redis, ConnectionError, DataError
import json


class RedisCache:
    def __init__(self, config: dict):
        self.config=config
        self.ttl=config['ttl']
        self.conn=self._connect()
    
    def _connect(self):
        try:
            conn = Redis(**self.config['redis'])
            return conn
        except ConnectionError as err:
            print(err)
            return None

    def get_value(self, name:str):
        data = self.conn.get(name)
        if data:
            value = json.loads(data)
            return value
        return None

    def set_value(self, name, value_dict: dict):
        try:
            value = json.dumps(value_dict)
            self.conn.setex(name,self.ttl,value)
            return True
        except DataError as err:
            print(err)
            return False