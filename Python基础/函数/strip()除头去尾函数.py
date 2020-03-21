# strip(chars)除头去尾函数：移除字符串头尾指定的字符（chars为空时则剔除所有空字符、换行符、制表符）或字符序列。
string='1234qwer4321'
print(string.strip('2431'))
string='   \n  \t qwer  \t  \n     '
print(string.strip())
# strip(chars)函数衍生出的两个函数：lstrip(chars)去除头部函数，rstrip(chars)去除尾部函数。
string='1234qwer4321'
print(string.lstrip('2431'))
print(string.rstrip('2431'))