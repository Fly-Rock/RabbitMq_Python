#coding=UTF-8

cars = ['audi','bmw','subaru']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

my_age = 18
your_age = 20
if my_age == 18 and your_age == 20:
    print("yong")
else:
    print("old")
    
if my_age > 10 or your_age > 10:
    print("you too")

#是否包含 判断
if 'audi' in cars:
    print("audi in the cars")
if 'a' not in cars:
    print("a not in the cars")
#if elif else
age = 18
if age < 4:
    print("You are < 4")
elif age < 18:
    print("You are 4 - 18")
else:
    print("You are >= 18")
"""
else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用 一个elif 代码块来代替else 代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。
"""
#非空判断list
none_list = []
if not none_list:
    print("none_list null")
else:
    print("none_list not  null")







