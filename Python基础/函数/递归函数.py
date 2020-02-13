# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，那么这个函数就是递归函数。
def test1(n):
  if n==1:
    return 1
  return n*test1(n-1)
print(test1(6))
# 使用递归函数需要注意防止栈溢出，解决递归调用栈溢出的方法是通过尾递归优化。
# 尾递归是指在函数返回的时候，调用自身本身，并且return语句不能包含表达式。
# n-1,n*result在调用函数前就会被计算，不会影响到函数。
def test2(n,result):
  if n==1:
    return result
  return test2(n-1,n*result)
print(test2(6,1))
