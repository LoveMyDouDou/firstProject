#-*-coding:utf-8-*-

import re
import requests

#读入源代码文件
f=open('source.html','r')
html=f.read()
f.close()

#匹配图片地址
pic_url=re.findall('img src="(.*?)" class="lessonimg"',html,re.S)
i=0
for each in pic_url:
    print 'now downloading:'+each
    pic=requests.get(each)
    fp=open('pic\\'+str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i+=1