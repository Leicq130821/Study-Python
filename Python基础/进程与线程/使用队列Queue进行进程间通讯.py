from multiprocessing import Process,Queue
from time import sleep
import random,os,datetime

def Write(Q):
    for i in range(5):
        sleep(random.random())
        Q.put(i)
        print('进程1:',os.getpid(),'往队列中写入数据:',i,datetime.datetime.now())
def Read(Q):
    while True:
        print('进程2:',os.getpid(),'从队列中取数据:',Q.get(),datetime.datetime.now())
if __name__ == '__main__':
    Q=Queue()
    Process1=Process(target=Write,args=(Q,),name='进程1')
    Process2=Process(target=Read,args=(Q,),name='进程2')
    Process1.start()
    Process2.start()
    Process1.join()
    Process2.terminate()