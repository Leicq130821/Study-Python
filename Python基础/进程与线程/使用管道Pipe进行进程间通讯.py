from multiprocessing import Process,Pipe
from time import sleep
import datetime,os,random

def send(pipe):
    for i in range(5):
        sleep(random.random())
        pipe.send(i)
        print('进程1:',os.getpid(),'发送数据：',i,datetime.datetime.now())
def recv(pipe):
    while True:
        print('进程2:',os.getpid(),'接收数据：',pipe.recv(),datetime.datetime.now())
if __name__ == '__main__':
    pipe=Pipe(duplex=False)
    Process1=Process(target=send,args=(pipe[1],),name='进程1')
    Process2=Process(target=recv,args=(pipe[0],),name='进程2')
    Process1.start()
    Process2.start()
    Process1.join()
    Process2.terminate()