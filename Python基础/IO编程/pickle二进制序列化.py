import pickle
# 变量的序列化
Dict=dict(name='LiMing',age=20,addres='浙江省温州市泰顺县')
Pickle=pickle.dumps(Dict)
print(Pickle)
# 序列化变量写入文件
with open(r'D:\Python\pickle.txt','wb') as file:
    pickle.dump(Dict,file)
# 变量的反序列化
print(pickle.loads(Pickle))
# 从文件中读取序列化变量数据
with open(r'D:\Python\pickle.txt','rb') as file:
    Pkdict=pickle.load(file)
    print(Pkdict)