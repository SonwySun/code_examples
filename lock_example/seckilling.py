import os
import redis

HOT_KEY = 'count'
r = redis.Redis(host='10.40.110.90', port=6379)


def seckilling():
    name = os.getpid()
    r.set('aaa', 1, nx=True, px=10000)
    v = r.get(HOT_KEY)
    if int(v) > 0:
        print(name, ' decr redis.')
        r.decr(HOT_KEY)
    else:
        print(name, ' can not set redis.', v)

def init_redis():
    r.set(HOT_KEY, 1)
