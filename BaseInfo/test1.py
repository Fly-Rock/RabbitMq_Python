#coding=UTF-8

from collections import OrderedDict
from random import randint

dic = OrderedDict()
dic['jerry'] = 'Python'
dic['zhangsan'] = 'java'
dic['lisi'] = 'c#'

for name,lang in dic.items():
    print(name + " like " + lang)

x = randint(1,6)
print(x)

