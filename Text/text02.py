
# i=0
# while i<10:
#     print(i,end=" ")
#     i+=1
#
# a=50
#
# print(a)
# print(a)
# if a>(i+41):
#     a+=i下·
#     print(a)
# elif i>55:
#     print("50")
# else:
#     print("nihao ")

def printme(name,*,age):
    print("年龄为：",age)
    print("名字为：",name)
    return

printme("wld",age=14)