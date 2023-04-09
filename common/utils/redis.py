from django.conf import settings
from redis import StrictRedis


class RedisUtils:
    def __init__(self):
        self.node = StrictRedis(
            host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB, decode_responses=True
        )

    def get_value_from_key(self, key):
        return self.node.get(name=key)

    def set_value_in_key(self, key, value, expiry):
        return self.node.set(name=key, value=value, ex=expiry)
