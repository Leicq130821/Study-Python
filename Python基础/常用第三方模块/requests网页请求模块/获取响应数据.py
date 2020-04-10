import requests

response=requests.get('http://192.168.100.233:7003')
# 响应内容的编码格式，也可以对响应内容设置编码格式（response.encoding='utf-8'）。
print(response.encoding)
# 字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
print(response.text)
# 以字节形式（二进制）返回，字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
print(response.content)
# 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None。
print(response.headers)
# 响应状态码。
print(response.status_code)
# 返回原始响应体，也就是urllib的response对象。
print(response.raw)
# 返回布尔值，表示请求是否成功。
print(response.ok)
# Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常。
print(response.json)
# 失败请求(非200响应)抛出异常。
print(response.raise_for_status())