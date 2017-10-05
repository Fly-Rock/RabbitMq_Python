#coding=utf-8


user_list = ["lichuanjie","zhangsan","li wang"]


user_list.insert(0,"firt one")#insert first one
user_list.insert(1,"second one")
user_list.append("last one")#insert last one after
print("----last two item----")
print(user_list[-1])#last one item
print(user_list[-2])#last second one

print("----for item list----")
for x in user_list:
	print(x)


#delete item
print("----delete item-----")
del user_list[-1]
del user_list[0]
print(user_list)

#pop del item 删除之后返回 删除掉元素值
print("------pop del item 删除之后返回 删除掉元素值----")
pop_last_one = user_list.pop()# 删除最后一个
print(user_list)
pop_send_one = user_list.pop(1)# 删除第二个
print("-----pop_delete_send_one:" + pop_send_one)
print(user_list)
## remove 删除指定的值

#user_list.remove("122")# 删除 不存在的 值 会报错

user_list.append("78")

message = "my emset "


message.split()
print(message)
#sort and sorted sort 永久排序变化 sorted仅仅临时排序，不改变之前的排序
num_list = [1,4,5,10,67,100,33]
num_list.sort()
print(num_list)
#sort 正序 sort(reverse=True) 倒序
num_list.sort(reverse=True)
print(num_list)

sorted_list = [34,1,65,20]
print(sorted(sorted_list))
print(sorted_list)

# list 元素颠倒
reverse_list = ["A","B","C"]
reverse_list.reverse()
print(reverse_list)
#list len 长度计算
print(len(reverse_list))




















