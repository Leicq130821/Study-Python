import requests

# requests.get(url,params,kwargs)get请求：url地址，param参数，kwargs其他数据如果全部放在一起则需要整理成字典格式。
requests.get('http://192.168.100.233:7003')
# get请求可以添加参数，参数可以放在URL里面，URL问号后面的内容就是参数以及参数值，多个参数之间用&隔开。
# 参数也可以放在params，格式为字典或者json，这两种效果实现是一样的。
response1=requests.get('http://192.168.100.233:7003/transaction/project/product_set.jsp?product_id=856&contract_id=200')
response2=requests.get('http://192.168.100.233:7003/transaction/project/product_set.jsp?',params={'product_id':856,'contract_id':200})
print(response1.url)
print(response2.url)