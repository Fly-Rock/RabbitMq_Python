#coding:UTF-8

print("hello world")
#:set number 
#:q! no save  
#:wq save
# 如果文件readonly 可以：输入  :set noreadonly
"""
学习插入模式
1)正常模式==》命令模式：shift+;
2)正常模式==》可视模式：v 可视模式  V 可视块模式
3)正常模式==>插入模式    
     按 i   在光标前插入    
     按 I   在行首插入 
     按 a   在光标后插入 
     按 s   删除光标所在的字符再插入
     按 A 在行末插入    
     按 o   在当前行之下新建行   
     按 O 在当前行之上新建行
     按 S   删除光标所在行再插入
4)其它模式==>正常模式    
     按 Esc键
"""


"""
定位命令总结：
h：左移一个字符
j：下一行
k：上一行
l：右移一个字符
$：移动到行尾
0：移动到行首
H：移至屏幕上方
M：移至屏幕中间
L：移至屏幕下方

：set  nu ：设置显示文本的行数
：set  nonu：取消显示文本的行数
gg：移到文件的行首
G：移到最后一行
：n：移到文件的第n行（与nG的功能相同）命令模式下面：
正常模式下面按  nG 到第n 行
"""
print("中文")



#INIEIIEIIE
#I am jerry,what do you do 
I
#DJINIE INN

