#coding=UTF-8

message = input("Tell me something,and I will repeat it back to you:")

print(message)

age = input('How old are you?')
age = int(age)
if age > 18:
    print("You are too old")
else:
    print("You are too young")

#让用户选择退出
print("input 'exit' end the program.")

message = ""
while message != "exit":
    message = input("tell me someting about you:\n")
    if message != 'exit':
       print(message)
#使用break 退出循环
while True:
    city = input("please input city")
    if city == 'exit':
        break
    else:
        print(city)
#使用continue
current_number = 10
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0
       continue
    print(current_number)

    

