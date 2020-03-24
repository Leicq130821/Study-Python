# 不使用进程来调用函数，那么运行顺序是函数1执行之后才会调用函数2，依次按照顺序来运行。
import datetime,random,os
from time import sleep

def func1(funcname):
    for i in range(5):
        sleep(random.random())
        print(funcname,'在执行',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
def func2(funcname):
    for i in range(5):
        sleep(random.random())
        print(funcname,'在执行',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
if __name__ == '__main__':
    # 开始运行进程
    func1('函数1')
    func2('函数2')
    print('main')
