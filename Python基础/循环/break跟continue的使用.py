# break跳出并终止循环
sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
    if i==5:
        break
print(sum)
# continue跳出当前循环，进入下一个循环。
n=0
while n<10:
    n+=1
    if n%2==0:
        continue
    print(n)