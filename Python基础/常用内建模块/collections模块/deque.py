from collections import deque

List=['a','b','c','d']
Deque=deque(List)
print(Deque)
# 左增
Deque.appendleft(1)
print(Deque)
# 左边扩展
Deque.extendleft([1,2,3])
print(Deque)
# 左弹出
Deque.popleft()
print(Deque)