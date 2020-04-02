import threading,datetime,random
from time import sleep

def func1(Thread):
    for i in range(5):
        sleep(random.random())
        print('线程',Thread,':',threading.current_thread(),'正在执行',datetime.datetime.now())
def func2(Thread):
    for i in range(5):
        sleep(random.random())
        print('线程', Thread, ':', threading.current_thread(), '正在执行', datetime.datetime.now())
if __name__ == '__main__':
    print(threading.current_thread())
    Thread1=threading.Thread(target=func1,args=('线程1',))
    Thread2=threading.Thread(target=func2,args=('线程2',))
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()