# -*- coding: UTF-8 -*-
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(2)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    print 111
    p.join()
    print 'All subprocesses done.'

# import time
# from multiprocessing import Pool
# def run(fn):
#   #fn: 函数参数是数据列表的一个元素
#   time.sleep(1)
#   return fn*fn
#
# if __name__ == "__main__":
#   testFL = [1,2,3,4,5,6]
#   print 'shunxu:' #顺序执行(也就是串行执行，单进程)
#   s = time.time()
#   for fn in testFL:
#     run(fn)
#
#   e1 = time.time()
#   print "顺序执行时间：", int(e1 - s)
#
#   print 'concurrent:' #创建多个进程，并行执行
#   pool = Pool(5)  #创建拥有5个进程数量的进程池
#   #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
#   rl =pool.map(run, testFL)
#   pool.close()#关闭进程池，不再接受新的进程
#   pool.join()#主进程阻塞等待子进程的退出
#   e2 = time.time()
#   print "并行执行时间：", int(e2-e1)
#   print rl