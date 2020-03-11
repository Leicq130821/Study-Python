# __slots__变量用来定义限制实例能够添加的属性。
class Test():
    __slots__ = ('name','address')
    pass
instance=Test()
instance.name='父类名称属性'
instance.address='父类地址属性'
# __slots__的限制属性只对当前类的实例有效，对继承了该类的子类的实例无效。
# 如果子类也定义了限制的类，那么子类的实例只能添加子类限制的属性以及父类限制的属性。
class Child(Test):
    __slots__ = ('age','sex')
    pass
child=Child()
child.name='子类名称属性'
child.address='子类地址属性'
child.age='子类年龄属性'
child.sex='子类性别属性'