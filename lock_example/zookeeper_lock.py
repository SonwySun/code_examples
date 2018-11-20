from datetime import datetime
from multiprocessing import Pool
from kazoo.client import KazooClient
from seckilling import seckilling, init_redis


def run_with_zk_lock(name):
    zk = KazooClient()
    zk.start()
    lock = zk.Lock("/lockpath", "my-identifier")
    while True:
        if datetime.now().second % 5 == 0:
            with lock:
                seckilling()
                return


if __name__ == '__main__':
    init_redis()
    p = Pool(16)
    for i in range(16):
        p.apply_async(run_with_zk_lock, args=(i,))
    print('now 16 processes are going to get lock!')
    p.close()
    p.join()
    print('All subprocesses done.')
