# 使用进程来调用函数可以实现并发。
from multiprocessing import Process
import datetime,random,os
from time import sleep

def func1(ProcessName):
    for i in range(5):
        sleep(random.random())
        print(ProcessName,'(',os.getpid(),')','在执行',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
def func2(ProcessName):
    for i in range(5):
        sleep(random.random())
        print(ProcessName,'(',os.getpid(),')','在执行',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
if __name__ == '__main__':
    Process1=Process(target=func1,args=('进程1',),name='进程1')
    Process2=Process(target=func2,args=('进程2',),name='进程2')
    # 开始运行进程
    Process1.start()
    Process2.start()
    Process1.join()
    Process2.join()
    print('main')
