# list函数生成列表
tuple=('a',1,'b',2)
set={1,'a',2,'b'}
print(list(range(10)))
print(list(tuple))
print(list(set))
# for循环创建列表
print([ x for x in range(10)])
# for循环还可以接受表达式，表达式写在for前面。
print([x*x for x in range(1,5)])
# for循环还可以使用两层循环
print([m+n for m in range(5) for n in range(5,10)])
# for循环后面还可以加上判断
print([x*x for x in range(1,10) if x%2==0])
# 如果想要使用if......else 必须要把判断语句写到for前面，不能写在for的后面
print([x if x>=0 else -x for x in [0,-1,2,-3,4]])