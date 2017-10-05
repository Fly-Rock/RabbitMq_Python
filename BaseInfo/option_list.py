#codeing=UTF-8
print("-----学习操作列表------")

#range() 函数的使用
#01 打印 1-5 数字
for value in range(1,6):
    print(value)

#使用range() 函数创建数字列表
num_list = list(range(0,11))
print(num_list)

#使用range() 可以指定步长
even_numbers = list(range(1,20,3))# 从1 开始 +3 到 20 结束：[1, 4, 7, 10, 13, 16, 19]
print(even_numbers)
#squares 计算数值平方值 1-10
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print("普通方法：" + str(squares))#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#上面的计算方值需要4行代码，能否更好的代码完成：神奇，列表解析
square_list = [value ** 2 for value in range(1,11)]
print("列表解析方法代码更少：" + str(square_list))
#对数字执行简单的统计计算
digit_numbers = list(range(0,101))
print(digit_numbers)
print("min:" + str(min(digit_numbers)) + "\nmax:" + str(max(digit_numbers)) + "\nsum:" + str(sum(digit_numbers)))
#3的倍数
three_num = []
for value in range(3,31):
    if(value % 3 == 0):
        three_num.append(value)
    else:
        pass

print(three_num)
#使用列表的一部分:切片功能 [m,n] 起始索引指定为m,并将终止索引指定为n,不包含n
abc = ['A','B','C','D','E','F']
print(abc[0:3])#['A','B','C']
print(abc[1:3])#['B','C'] 不包含最后一个索引位置
print(abc[-3:])#['D','E','F'] 最后三个
#复制列表操作
my_foods = ['apple','rice']
your_foods = my_foods[:]
my_foods.append("my meat")
your_foods.append("your meat")
print(my_foods)
print(your_foods)

#另一种复制操作
other_copy = ['one','two']
your_copy = other_copy
other_copy.append('three')
your_copy.append('four')
print(other_copy)
print(your_copy)
#元组操作







