# 类与实例可以绑定新的属性及方法，如果绑定在类上，那么通过该类创建的所有实例都可以进行访问。
# 如果绑定在实例删，那么绑定的属性及方法是实例独立的，其他实例不能进行访问。
from types import MethodType

class Test():
    pass
def mult(self,x,y):
    print(x*y)
def sum(self,x,y):
    print(x+y)
instance=Test()
Test.name1='属性名称1'
instance.name2='属性名称2'
instance.mult=MethodType(mult,instance)
Test.sum=sum

print(instance.name2)
print(instance.name1)
print(Test.name1)
Test().sum(10,100)
instance.sum(10,100)
instance.mult(10,11)
# 删除属性与方法
del instance.name2
del instance.mult
del Test.name1
del Test.sum