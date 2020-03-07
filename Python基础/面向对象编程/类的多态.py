# 当子类的方法与父类存在相同的方法时，子类的方法会覆盖父类的方法。
from Python基础.面向对象编程.class类 import Classname

class Jicheng(Classname):
    def mult(self,x,y):
        print(x,'乘以',y,'等于',x*y)
    def sum(self,x,y):
        print(x,'加',y,'等于',x+y)

instance=Jicheng()
instance.mult(5,6)
instance.sum(5,6)

def run(func,x,y):
    func.mult(x,y)
    func.sum(x,y)

run(Classname(),5,6)
run(Jicheng(),5,6)