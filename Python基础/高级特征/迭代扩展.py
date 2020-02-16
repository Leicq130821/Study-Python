# 通过collections.abc模块的Iterable类型来判断对象是否可以进行迭代。
list=list(range(0,10,2))
tuple=('a','b','c')
set={'a',1,'b',2}
int=123456
str='a1b2'
a=('a','b','c')
b=(1,2,3)
dict=dict(zip(a,b))
from collections.abc import Iterable
print(isinstance(list,Iterable))
print(isinstance(tuple,Iterable))
print(isinstance(set,Iterable))
print(isinstance(int,Iterable))
print(isinstance(str,Iterable))
print(isinstance(dict,Iterable))
# enumerate(Iterable,start=开始下标) 函数用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标。
# （注意：开始下标并不是迭代数据的开始时游标，只是起到一个开始编号的作用）
for i,value in enumerate(tuple):
    print(i,':',value)
for i,value in enumerate(str,start=2):
    print(i,':',value)