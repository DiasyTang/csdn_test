import time
import json
import random
import gevent
from gevent import monkey

monkey.patch_socket()


def call_gevent(run, count):
    begin_time = time.time()
    run_gevent_list = [gevent.spawn(run, i) for i in range(count)]
    gevent.joinall(run_gevent_list)
    end = time.time()
    print("单次测试时间（平均）s:", (end - begin_time) / count)
    print("累计测试时间 s:", end - begin_time)


if __name__ == "__main__":
    run = lambda n: print("task is %s" % n)
    call_gevent(run, 1000)

