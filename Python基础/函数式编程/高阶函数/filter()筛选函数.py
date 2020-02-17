# filter(function, iterable)：函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 需要两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
a={1,2,3,4,5,6}
result=filter(lambda x:x%2==1,a)
print(list(result))

def test(x):
    return x%2==0
print(list(filter(test,range(10))))