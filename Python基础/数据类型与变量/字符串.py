# 字符串需要用单引号或者双引号括起来。
print("abc")
print('我爱中国！')
# 可以通过索引来访问字符串某个字符
str='我爱中国！'
print(str[0])
# 字符串单引号括内容引号只能用双引号，双引号括内容只能用单引号。
print('"abc""def"')
print("'qwe''rty'")
# 字符串内容既包含单引号又包含双引号需要用\转义符
print('I\'m a \"teacher\"')
# \为转义符，\t为制表符，\n为换行符，\\为\
print('\t111\n\\')
# python用'''...'''表示多行内容
print('''line1
line2
line3''')