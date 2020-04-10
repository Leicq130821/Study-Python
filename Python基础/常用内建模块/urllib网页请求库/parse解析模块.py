from urllib import parse
# (1)urlpase()：解析url。
result=parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')
print(result.scheme,result[0])
print(result.netloc,result[1])
print(result.path,result[2])
print(result.params,result[3])
print(result.query,result[4])
print(result.fragment,result[5])
# (2)urlunparse()：合成一个url.
List=['https','128.8.18.233:7001','/investment/invest/contract.jsp','','book_code=1&contract_id=200','']
url=parse.urlunparse(List)
print(url)
# (3)urlsplit()：与urlparse()方法类似，它会返回5个部分，把params合并到path中。
result=parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result,sep='\n')
print(result.scheme,result[0])
print(result.netloc,result[1])
print(result.path,result[2])
print(result.query,result[3])
print(result.fragment,result[4])
# (4)urlunsplit()：与urlunparse()类似，唯一的区别是长度必须是5个，它省略了params。
Tuple=('https','128.8.18.233:7001','/investment/invest/contract.jsp','book_code=1&contract_id=200','')
url=parse.urlunsplit(Tuple)
print(url)
# (5)urljoin(base_url,url)：通过将基本URL（base）与另一个URL(url)组合起来构建完整URL，它会使用基本URL组件，协议(schemm)、域名(netloc)、路径(path)、来提供给URL中缺失的部分进行补充，最后返回结果。
URL=parse.urljoin('https://127.0.0.1:9081/project/forms/invest.jsp?busi_id=120305&invest_id=90','http://128.8.18.233:9080/investment/invest/contract.jsp?product_id=1000&contract_id=20')
url=parse.urljoin('http://128.8.18.233:9080/investment/invest/contract.jsp','?product_id=1000&contract_id=20')
print(url)
print(URL)
# (6)urlencode()：在构造GET请求参数时很有用，它可以将字典转化为GET请求参数。
Dict={'product_id':1000,'contract_id':20}
url='http://128.8.18.233:9080/investment/invest/contract.jsp?'+ parse.urlencode(Dict)
print(url)
# (7)parse_qs()：与urlencode()正好相反，它是用来反序列化的，如将GET参数转换回字典格式。
Dict=parse.parse_qs('product_id=1000&contract_id=20')
print(Dict)
# (8)parse_qsl()：将参数转换为元组组成的列表。
List=parse.parse_qsl('product_id=1000&contract_id=20')
print(List)
# (9)quote()：按照标准，URL只允许一部分ASCII字符（数字字母和部分符号）。
# 其他的字符或者汉字是不符合URL标准的，所以URL中使用其他字符就需要进行URL编码，quote()函数提供了此功能。
value=parse.quote('汉字')
url='http://127.0.0.1:9080//investment/invest/contract.jsp?name='+value
print(url)
# (10)unquote()：与quote()相反，用来进行URL解码。
print(parse.unquote(value))