#coding=utf-8

#导入re库文件
import re

secret_code='hadfalifexxIxxfasdjifja134xxlovexx2345xxyouxx8dfse'

# .的使用:占位符
a='xz123'
b=re.findall('x...',a)
print b


# *的使用
a='xyxy123'
b=re.findall('x*',a)
print b

# ?的使用,匹配0次或1次
a='xy123'
b=re.findall('x?',a)
print b

'''
需要掌握组合方式(.*?)
'''

# .*的使用举例
b=re.findall('xx.*xx',secret_code)
print b

# .*?使用举例
c=re.findall('xx.*?xx',secret_code)
print c


#使用括号与不适用括号的举例
d=re.findall('xx(.*?)xx',secret_code)
print d
for each in d:
    print each

s='''sdfxxhello
xxfsdfxxworldxxasdf
'''
d=re.findall('xx(.*?)xx',s,re.S)
print d


#对比findall与search的区别
s2='asdfxxIxx123xxlovexxdfd'
f=re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
print f

f2=re.findall('xx(.*?)xx123xx(.*?)xx',s2)
print f2[0][1]


#sub的使用
s='123abcsrrrrsfasdfas123'
output=re.sub('123(.*?)123','123%d123'%789,s)
print output


#匹配纯数字
a='asdfasf1234567fasdfas'
b=re.findall('(\d+)',a)
print b


