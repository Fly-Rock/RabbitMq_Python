
print("hello world python")

user_name = "li chUan jie"
print(user_name.title())
print(user_name.upper())
print(user_name.lower())

#python 注释
"""
print("中文")
i am more 

"""


print("\tpython")

print("\t\t java")

print("c# \n java \n javascript")
#消除空白 删除 左右两边空白 strip() 删除左边空白 lstrip() 删除右边空白 rstrip()

name1 = "zhang"
name2 = "zhang "
name3 = " zhang "
print(name2)
print(name2.rstrip())
print(name2==name1)#false
print(name2.rstrip()==name1.rstrip())#ture

# 字符串语法错误情况 符号问题
#print('122';')

#print("2333"3")

"""
python 运算
"""

# 两个乘号代表 乘方计算
print(3**3)#27
print(4**3)#64

#int 转 字符
age = 18
#下面会报错
#message = "I am "+ age + "years" 
#正常需要转换
message =  "I am "+ str(age) + " years" 
print(message)

#相除
#3/2=1
#3/2.0=1.5
#3.0/2=1.5
#3.0／2.0=1.5


def add_start():
    a = 1
    b = 2
    if a == b:
        print("a == b")
    else:
        print("a!=b")
