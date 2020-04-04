import re

# re.compile(pattern,flag):正则表达式对象化函数，可以将正则表达式对象化，正则表达式对象可以使用match()、search()等函数匹配字串符。
Regex=re.compile(r'\d+\w{2}')
print(Regex.search('abc12def'))
print(Regex.search('abc12def').group())
# re.search(pattern,string,flag):扫描字符串以查找正则表达式模式产生匹配项的第一个位置，然后返回相应的match对象。如果字符串中没有与模式匹配，则返回None。
print(re.search(r'e\d{2}\w+','q12w3e45_t67'))
print(re.search(r'e\d{2}\w+','q12w3e45_t67').group())
# re.match(pattern,string,flag):与search()函数区别在于匹配时要从字符串的第一个字符开始匹配，如果匹配不到则返回None。
print(re.match(r'e\d{2}\w+','q12w3e45_t67'))
print(re.match(r'e\d{2}\w','e45_t67').group())
# re.fullmatch(pattern，string，flag=0):如果整个字符串与正则表达式模式匹配，则返回相应的match对象。
print(re.fullmatch(r'a\w{2}\d{3}','qabc123456'))
print(re.fullmatch(r'a\w{2}\d{3}','abc123').group())
# re.split(pattern,string,maxsplit=0,flag=0):支持正则表达式的拆分函数，maxsplit为切割次数。
print(re.split('\W', 'Words, words, words.')) #\W为非字母数字下划线