# 如果给定一个list或tuple，可以通过for循环来遍历这个list或tuple，这种遍历称为迭代。
liebaio=(list(range(0,10,2)))
for i in liebaio:
    print(i)
# python可以进行迭代的对象不仅局限于list或tuple，dict、set、str也可以进行迭代。
a=['a','b','c']
b=[1,2,3]
zidian=dict(zip(a,b))
for key in zidian.keys():
    print(key,':',zidian[key])
for value in zidian.values():
    print(value)
for key,value in zidian.items():
    print(key,':',value)
set={'a','b',1,2}
for yuansu in set:
    print(yuansu)
str='abc'
for s in str:
    print(s)