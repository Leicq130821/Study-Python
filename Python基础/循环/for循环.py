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