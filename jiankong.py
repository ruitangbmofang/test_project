#coding=utf-8
from __future__ import unicode_literals
# import time
# import psutil as pu 
# a = pu.cpu_times()
# print a
# # print pu.net_io_counters()
# # print pu.cpu_count(logical=False)
# # print pu.swap_memory().free/1024/1024/1024
# # print pu.net_io_counters().bytes_recv/1024/1024
# print pu.virtual_memory().free/1024/1024


import redis

r = redis.Redis(host='192.168.3.124',port=6379,db=0)

keys = r.flushall()

