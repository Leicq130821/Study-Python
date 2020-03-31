# 类与实例可以绑定新的属性及方法，如果绑定在类上，那么通过该类创建的所有实例都可以进行访问。
# 如果绑定在实例上，那么绑定的属性及方法是实例独立的，其他实例不能进行访问。
from types import MethodType

class Test():
    pass
def mult(self,x,y):
    return x*y
def sum(self,x,y):
    return x+y

Test.mult=mult

Test.name='类的名称'
Instance1=Test()
Instance2=Test()
Instance2.name='实例2的名称'
print(Test.name)
print(Instance1.name)
print(Instance2.name)
Instance2.sum=MethodType(sum,Instance2)
print(Instance1.mult(3,4))
print(Instance2.sum(1,99))
print(Instance2.mult(4,5))