#coding=UTF-8 
import json

file_path = 'python_test.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

#逐行读取
with open(file_path) as file_obj:
    for line in file_obj:
        print(line.rstrip())

#创建一个包含文件各行内容列表
with open(file_path) as file_content:
    lines = file_content.readlines()

print("---new lines----")
for line in lines:
    print(line.rstrip())


#write file_object

with open(file_path,'w') as file_write:
    for item in range(0,10000):
        file_write.write(str(item)+"\n")

#try
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("需要正确执行的代码")
    
#json.dump() json.load()
json_str = {
        "name":"jerry",
        "age":12
        }
file_name = 'json.json'
with open(file_name,'w') as file_json:
    json.dump(json_str,file_json)



with open(file_name) as file_load:
    load_json = json.load(file_load)
print(load_json)









