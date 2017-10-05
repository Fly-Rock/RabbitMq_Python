#coding=UTF-8

#函数关键字实体参数
def desc_person(name,age=12):
    print("I name is " + name.title() + " and I am  " + str(age) + " years old ")

desc_person(age=12,name="jerry")
#禁止函数修改列表

#传递任意数量的实参
def make_pizza(*toppings):
    for value in toppings:
        print(value)

make_pizza("A","B","C")

#结合使用位置实参和任意数量实参

def make_pizza(size,*toppings):
    print(size)

def make_car(name,back,**info):
    list = {}
    list["name"] = name
    list["back"] = back
    for key,value in info.items():
        list[key] = value
    return list


cars = make_car("subaru","outback",color="bule",tow_pack=True)
print(cars)


