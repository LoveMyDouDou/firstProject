#coding=utf-8


#单引号
c1='2ght'
print c1
c2='It is a "dog" !'
print c2


#双引号
c1="2ght"
print c1
c2="It's a dog!"
print c2

#三引号
c1='''he
she
is my
hello
'''
print c1

c1="""he
she
is my
hello
"""
print c1


#转义符
print 'It\'s a dog!'
print "hello boy\nhello boy"


#自然字符串
print "hello boy\nhello boy"
print r"hello boy\nhello boy"

#字符串的重复
print "I love my DouDou\n"*999

#子字符串
#索引运算符从0开始索引
#切片运算符[a:b]是指从下标a开始到下标b-1。同样第一位下标为0
str="I love my DouDou"
substr=str[0];
print  substr
substr=str[2];
print  substr
substr=str[4];
print  substr
substr=str[2:6]
print  substr
