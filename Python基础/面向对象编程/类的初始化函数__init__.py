class Test:
    # 类的初始化函数
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sum(self):
        return self.x+self.y+self.z
    def mix(self):
        return self.x*self.y*self.z
# 如果类的初始换函数含有除了self之外的参数，那么类的实例化需要传入这些参数。
test=Test(2,3,4)
print(test.sum())
print(test.mix())