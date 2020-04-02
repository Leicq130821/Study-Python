from multiprocessing import Pool
import os,datetime,random
from time import sleep

def func(n):
    for i in range(5):
        sleep(random.random())
        print('第',n,'个进程(ID：',os.getpid(),')','在执行',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
if __name__ == '__main__':
    Process=Pool(4)
    for n in range(1,5):
        Process.apply_async(func,args=(n,))
    Process.close()
    Process.join()
    print('main')