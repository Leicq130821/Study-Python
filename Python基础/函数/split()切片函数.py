# split(str,num)拆分函数：通过指定分隔符对字符串进行切片，如果参数num有指定值，则分隔num+1个子字符串,返回一个列表。
# str：分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)。num：分割次数，默认为 -1, 即分隔所有。
string1='abc \ndef \n\tghi'
string2='abc+def+ghi'
print(string1.split())
print(string1.split(' '))
print(string1.split('\n'))
print(string1.split(' ',2))
print(string2.split('+'))