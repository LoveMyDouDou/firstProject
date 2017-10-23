#coding=utf-8


# # 列表
# students=["小明","小红","小李","小云"]
# print students[0]
#
# students[0]="小月"
# print students[0]


# students=("小明","小红","小李","小云")
#
# students[0]="小月"
# print students[0]

# a=set("abcnmaaaagsng")
# b=set("cdfm")
#
# print a
# #交集
# x=a&b
# print x
#
# #并集
# y=a|b
# print y
#
# #差集
# z=a-b
# print z
#
# #去除重复元素
# new=set(a)
# print new


# #字典
# k={"姓名":"微微","籍贯":"桂林"}
# print k["籍贯"]
#
# #添加字典里面的项目
# k["爱好"]="音乐"
# print k["姓名"]
# print k["爱好"]


# #标识符命名原则
# ssd_1=32
# print  ssd_1
#
# _1ssd=223
# print _1ssd

# import pickle
#
# #dumps(object)将对象序列化
# lista=["mingyue","jishi","you"]
# listb=pickle.dumps(lista)
# print listb
#
#
# #loads(string)将对象原样恢复，并且对象类型也恢复为原来的格式
# listc=pickle.loads(listb)
# print listc
#
# #dump(object,file)，将对象存储到文件里面序列化
# group1=("bajiu","wen","qingtian")
# f1=file('1.pk1','wb')
# pickle.dump(group1,f1,True)
# f1.close()
#
# #load(object,file)将dump()存储文件里面的数据恢复
# f2=file('1.pk1','rb')
# t=pickle.load(f2)
# print t
# f2.close()




# #逻辑行与物理行
#
# #以下是3个物理行
# print "abc"
# print "789"
# print "777"
#
# #以下是1个物理行，3个逻辑行
# print "abc" ; print "789" ; print "777"
#
# #以下是1个逻辑行，3个物理行
# print '''我其实
# 是一个
# 逻辑行
# '''


# #分号使用规则
#
# #所欲的逻辑行后均应使用分号，但以下条件除外
# print "123"; print "456";
# print "777";
#
# #分号可以省略的条件是指:每个物理行的行末可以省略分号，当然也可以不省略分号。
# print "123"; print "456"
# print "777"


# #行连接
# print  "我是一行\
# 显示"


# a="777"
# print a

# #如何缩进
#
# #一般情况下，行首应该不留空白
# import sys
#
# #缩进的方法有两种，可以按空格；也可以按Tab键
#
# #if语句的缩进方法
# a=7
# if a>0:
#     print "hello"
#
# #while语句的缩进方法
# a=0
# while a<7:
#     print a
#     a+=1

#"+":两个对象相加
#两个数字相加
# a=7+8
# print a
#
# #两个字符串相加
# b="GOOD"+" JOB!"
# print b
#
# #"-":取一个数的相反数或者实现两个数字相见
# a=-7
# print a
# b=-(-8)
# print b
#
# c=19-1
# print c
#
#
# #"*":两个数相乘或者字符串重复
# a=4*7
# print a
#
# b="hello"*7
# print b
#
#
# #"/":两个数字相除
# a=7/2
# print a
#
# b=7.0/2
# c=7/2.0
# print b
# print c
#
# #"求幂运算"
# a=2**3  #相当于2的3次幂
# print a
#
# #"<":小于符号，返回一个bool值
# a=3<7
# print a
#
# b=3<3
# print b
#
#
# #"!="：不等于符号，同样返回一个bool值
# a=2!=3
# print a
#
# b=2!=2
# print b
#
# #"//"除法运算，然后返回其商部分，舍去余数
# a=10//3
# print a
#
#
# #"%":取模运算
# a=10%3
# print a
#
# b=10%1
# print b
#
# a=10//3
# b=10%3
# c=3*a+b
# print c
#
# #"&":按位与运算，所谓的按位的与运算是指一个数字转化为二进制，
# # 然后这些二进制的数按位来进行与运算
#
# a=7&18
# print a
#
#
# #"|":按位或运算，同样我们要将数字转化为二进制之后按位进行或运算
# a=7|18
# print a
#
#
# #"^"按位异或
# a=7^18
# print a
#
# #"~":按位翻转: ~x=-(x+1)
# a=~18
# print a
#
# #"<<":左移
# a=18<<1
# print a
#
# b=3<<3
# print b
#
# #">>"右移
# a=18>>1
# print a
#
# b=18>>2
# print b
#
# #"<="和">="
# a=5<=5
# print a
# b=6>=5
# print b
#
# #"=="比较两个对象是否相等
# a=12==13
# print a
#
# b="hello"=="hello"
# print b
#
# #not:逻辑非
# a=True
# b=not a
# print b
#
# #and:逻辑与
# print True and True
#
# #or:逻辑或
# print True or False


# #优先级的作用
# a=2+7*8
# print a
#
# b=9>7
# print b


# #优先级使用实战
#
# #优先级排行榜第1名--函数调用、寻址、下标
#
# #优先级排行榜第2名--幂运算
# a=4*2**3
# print a
#
# #优先级排行榜第3名--翻转运算~
#
# #优先级排行榜第4名--正负号
# print 2+4*-2
#
# #优先级排行第5名--*、/、%
# print 2+4*2/4
#
# #优先级排行榜第6名--+、-
# print 3<<2+1
#
# #优先级排行榜第7名-- <<、>>
#
# #优先级排行榜第8名-- 按位&、^、|，其实这三个中也是有优先级顺序的，但他们初一同意级别，故而不细分
#
# #优先级排行榜第9名--比较运算符
# a=2*3+5<=5+1*2
# print a
#
# #优先级排行榜第10名--逻辑的not、and、or
#
#
# #优先级排行榜第11名--lambda表达式


# #优先级使用规律
#
# #1、一般情况下是左结合的
# print 4+6+5*6+6
#
# #2、出现赋值的时候一般是右结合
# a=8+91
# print a


# a=(2+5)*6
# print a
# b=((2+5)+5)*6
# print b



# #什么是表达式
#
# #1
# "hello"
#
# #2
# 25+7
#
# #3
# a=67
# a
#
# #4
# a="hello"

# #控制流
#
# #控制流的功能
# #要实现:重复执行3段同样的程序
#
#
# #方式一:
#
# i=0
# print i
# i=i+1
# print i
#
# #方式二:
#
# for k in range(0,3):
#     i=0
#     print i
#     i=i+1
#     print i
#
# #再比如,要实现:如果小明吃了饭了，输出小明很乖，
# # 如果小明没有吃饭，输出小明不乖
#
# #平常情况按顺序执行的话，无法实现这样的功能，我们可以用控制流中的分支结构
#
# xiaoming="eat"
# if xiaoming=="eat":
#     print "小明很乖"
# else:
#     print "小明不乖"
#
#
# #控制流类型有三种，一种是顺序结构，一种是分支结构，一种是循环结构
#
# #顺序结构
#
# a=7
# print a
# a=a-1
# print a
# a=a+6
# print a
#
#
# #分支结构
# a=8
# if a==8:
#     print "She"
# else:
#     print "He"
#
#
# #循环结构
# a=7
# while a:
#     print "hello"
#     a-=1

# #if语句
# #if语句的格式用法:
#
# '''
# if 是这样:
#    执行该部分的语句
# elif 或者是这样:
#    执行elif部分语句
# else 或者以上情况都不是:
#    执行该部分语句
# '''
#
# #一种情况的if用法
# a=8
# if a==8:
#     print "hello"
#
# if a!=8:
#     print "hehe"
#
# #两种情况选择下的if用法
#
# a=8
# if a==8:
#     print "She"
# else:
#     print "He"
#
# #三种选择情况下的if用法
# a=8
# if a==7:
#     print "I"
# elif a>7:
#     print "he"
# else:
#     print "she"
#
# #if语句使用要点
# #各分支尽量不重复，并且尽量包含全部可能性
#
# a=80
# b=0
# if 0<a<80:
#     print "差"
# elif 80<=a<=100:
#     print "好"


# #while语句
# '''
# while 条件为真:
#     循环执行该部分语句
# else:
#     如果条件为假，执行该部分语句
# '''
# #else部分可以省略
#
#
# #第一个是最简单没有else部分的
# # a=True
# # while a:
# #     print "ABC"
#
# #第二个是有else部分的
# b=False
# while b:
#     print "ABC"
# else:
#     print "DEF"
#
#
# #再来看一下比较复杂一点的有嵌套的while语句
# a=1
# while a<10:
#     if a<=5:
#         print a
#     else:
#         print "hello"
#     a=a+1
# else:
#     print "test"



# #for语句
#
# '''
# for语句格式:
# for i in 集合:
#     执行该部分
# else:
#     执行该部分
# '''
#
#
# #第一个for语句
#
# for i in [1,2,8,9,0]:
#     print i
#
# #学会使用range函数，第二个for语句
# for i in range(1,7):
#     print "hello"
#     print i
#
# a=range(3,6)
# print a
#
# for i in range(1,12,3):
#     print i
#
# #最后看一个带嵌套的for语句
#
# for i in range(1,10):
#     if i%2==0:
#         print i
#         print "偶数"
#     else:
#         print i
#         print "奇数"


# #break语句
# #break语句语法
#
#
# #break语句在while循环中的应用
#
# a=1
# while a:
#     print a
#     a=a+1
#     if a==10:
#         break
#
# #break语句在for循环中
#
# for i in range(5,10):
#     print i
#     if i>7:
#         break
#
#
# #break语句在双层循环中
#
# a=10
# while a<=12:
#     a=a+1
#     for i in range(1,7):
#         print i
#         if i==5:
#             break



# #continue的使用
#
# #continue语句的使用
#
# #continue是终止该次循环，而不是终止该循环
#
# a=1
# while a<7:
#     a=a+1
#     if a==3:
#         continue
#     print a
#
#
# #continue语句在for循环中，并比较以下两个程序a和b
#
# #程序a
#
# for i in range(1,7):
#     if i==3:
#         continue
#     print i
#
# #程序b
#
# for i in range(1,7):
#     print i
#     if i==3:
#         continue
#
#
# #continue语句在双层循环语句中
#
# a=1
# while a<7:
#     a=a+1
#     if a==4:
#         continue
#     for i in range(7,10):
#         if i==9:
#             continue
#         print i



# #函数的功能
#
# #系统自带的函数
#
# #1.实现取字符串长度的功能
#
# a="hello my teacher"
# print len(a)
#
# #2.实现字符串的切割
# a="student"
# b=a.split("u")
# print b
#
# #3.自定义函数
# def a():
#     print "hello";print 777
# a()


#函数定义
#格式

'''
def 函数名():
    函数内容
'''

# #实例
# def function1():
#     a=8
#     print a


# #函数的形参与实参
#
# #参数概念
#
# a="abcdef"
# print len(a)
#
# #什么是形参
# def function1(a,b):
#     if a>b:
#         print a
#     else:
#         print b
#
# #什么是实参
#
# function1(1,3)
#
# #参数的传递
#
# #第一种，最简单的传递
#
# def function(a,b):
#     if a>b:
#         print "大"
#     else:
#         print "小"
# function(5,2)
#
# #第二种，赋值传递
#
# def function(a,b=6):
#     print a
#     print b
# function(2,5)
#
#
# #关键参数
# def function(a=1,b=6,c=7):
#     print a
#     print b
#     print c
# function(5)
# function(b=7,c=8)
# function(5,c=2,b=3)
# function(b=4,c=2,a=1)
#
# #要注意，参数不能冲突
# # function(b=2,c=3,2)


# #全局变量与局部变量
#
# #作用域
# # def func():
# #     i=8
# #
# # print i
#
# # print j
# j=9
# print j
#
#
# #局部变量
# def func2(a):
#     i=7
#     print i
# i=9
# func2(i)
# print i
#
# #全局变量
#
# def func3():
#     global i
#     i=7
#     print i
# i=9
# func3()
# print i


#
# #函数的调用与返回值
#
# #函数的调用
#
# def a():
#     i=1
# a()
#
# #函数的返回值
# '''
# 函数的返回值是通过return语句实现的
# '''
# #一个返回值的情况
# def test():
#     i=7
#     return i
# print test()
#
#
# #多个返回值的情况
# def test2(i,j):
#     k=i*j
#     return (i,j,k)
# x=test2(4,5)
# print x
#
# y,z,m=test2(4,5)
# print y


# #文档字符串
#
# def d(i,j):
#     '''
#     这个函数实现一个乘法运算。
#     :param i:
#     :param j:
#     :return:
#     '''
#     k=i*j
#     return k
#
# print  d.__doc__
# help(d)



# import math
# print math.pi

# import sys
# print sys.version
# print sys.executable
# print sys.getwindowsversion()
# print sys.modules.keys()

# from sys import version
# print version

# from sys import *
# print version
# print executable



# print __name__


# if __name__=='__main__':
#     print "It's main"
# else:
#     print "It's not main"


# import sys
# #查看模块功能列表
# print dir(sys)
# #文档说明
# print sys.__doc__
# print sys.platform

# d=[]
# print dir(d)
# c=['a','b']
# print dir(c)
