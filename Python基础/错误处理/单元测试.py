# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
def Test(x):
    if not isinstance(x,(int,float)):
        return '输入参数类型不正确，需要输入数值！'
    elif x>0:
        return x
    else:
        return -x
if __name__ == '__main__':
    print(Test('10'))
    print(Test('A'))
    print(Test('%'))
    print(Test(10))
    print(Test(-5))
    print(Test(0))