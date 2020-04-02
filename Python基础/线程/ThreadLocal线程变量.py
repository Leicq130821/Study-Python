import threading

def fun1(name):
    ThreadLocal.name=name
    fun2()
def fun2():
    print(threading.current_thread().name,'的参数为：',ThreadLocal.name,'\n')
if __name__ == '__main__':
    ThreadLocal=threading.local()
    Thread1=threading.Thread(target=fun1,args=('参数1',),name='线程1')
    Thread2=threading.Thread(target=fun1,args=('参数2',),name='线程2')
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()


