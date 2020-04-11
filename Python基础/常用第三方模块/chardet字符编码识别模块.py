import chardet

print(chardet.detect(b'Hello, world!'))
print(chardet.detect('中文'.encode('GBK')))
Bytes='中文'.encode('UTF-8')
print(Bytes)
Str=Bytes.decode()
print(Str)