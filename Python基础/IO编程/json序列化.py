import json
# 变量序列化
Dict=dict(name='LiMing',age=20,addres='浙江省温州市泰顺县')
Json=json.dumps(Dict,ensure_ascii=False)
print(Json)
# 序列化变量写入文件
with open(r'D:\Python\json.txt','w') as file:
    json.dump(Dict,file,ensure_ascii=False)
# 变量反序列化
print(json.loads(Json))
# 从文件中读取序列化变量数据
with open(r'D:\Python\json.txt','r') as file:
    Jsdict=json.load(file)
    print(Jsdict)