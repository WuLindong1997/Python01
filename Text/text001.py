
list01=[1,2,5,4,8,7]
print(list01[1],type(list01[1]),type(list01))
print("删除前的：",list01)
#删除列表元素
del list01[2]

print("删除后的：",list01)
list01.insert(1,8)
print(list01)
list01.pop(1)
print(list01)
t1=(1,2,3,"4")
print(t1)
t2=tuple(list01)
print(type(list01))
print(t2)
print(id(t2))
print(id(t2[1]))

dict01={1:"ok",2:"ff",3:"gg"}
dict02=dict01.copy();
print(dict01)
print(dict02)
del dict02[1]
print(dict01)
print(dict02)