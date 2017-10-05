#coding=UTF-8

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
alien_0['speed'] = 5
print(alien_0)

#删除字典值对
del alien_0['speed']
print(alien_0)
#遍历字典
user_0 = {
        'username':'jerry',
        'first':'li',
        'last':'jerry'
        }
for key,value in user_0.items():
    print("dic key:" + key + " dic value:" + value)
#遍历所有的key
for key in user_0.keys():
    print(key)
if 'first' in user_0.keys():
    print("firt in the user_list")
    
#按照顺序遍历key
for key in sorted(user_0):
    print(key.title())

#遍历values
for value in user_0.values():
    print(value)



