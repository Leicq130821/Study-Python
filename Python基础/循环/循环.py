# for..in循环取list、tuple
classmates=['小明','小红','小刚']
for mate in classmates:
    print(mate)
classmates=('小明','小红','小刚')
for mate in classmates:
    print(mate)
# 计算10以内奇数之和
counts=list(range(1,11,2))
print(counts)
sum=0
for count in counts:
    sum=sum+count
print(sum)
# while循环
sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
print(sum)
# break提前跳出循环
sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
    if i==5:
        break
print(sum)
# continue跳出当前循环，进入下一轮循环
n=0
while n<10:
    n+=1
    if n%2==0:
        continue
    print(n)