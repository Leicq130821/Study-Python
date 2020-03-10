# 创建一个新的类时可以继承现有的类，继承的好处是新的类将会获取被继承类的全部功能。
from Python基础.面向对象编程.class类 import Classname
from Python基础.面向对象编程.class类 import Classname2
class Jicheng(Classname):
    pass

instance=Jicheng()
instance.mult(5,6)
instance.sum(5,6)
# 类可以一级级传承下来，使用issubclass(ChildClass,(FatherClass1,FatherClass2))来检查ChildClass是否继承FatherClass。
print(issubclass(Jicheng,(Classname,object)))
# 类还可以多重继承，继承多个类
class More(Classname,Classname2):
    pass
instance2=More()
instance2.sum(1,99)
instance2.mult(10,10)
instance2.sub(100,2)
