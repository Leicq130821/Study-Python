from itertools import chain
import itertools

# chain(*iterable)：可以把多个迭代器拼接成一个迭代器。
Chain=chain([1,2,3,4],('a','b','c','d'))
for i in Chain:
    print(i)

itertools.compress()