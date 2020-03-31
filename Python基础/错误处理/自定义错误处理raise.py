# raise可以自定义抛出异常信息，当抛出异常时，异常后面的语句将不会执行。
def Diomod(x,y):
    try:
        if not(isinstance(x,(int,float)) and isinstance(y,(int,float))):
            raise TypeError('被除数或除数的类型不对！')
        if y==0:
            raise ValueError('除数不能为0！')
    except Exception as E:
        print('输入错误：',E)
    else:
        print('输入正确，结果为：',x/y)
if __name__ == '__main__':
    Diomod(10,0)
    Diomod('a',1)
    Diomod(10,2)