#coding:utf-8
'''
Created on 2017年4月19日

@author: loye66
'''

import urllib2
from lib2to3.pgen2.tokenize import cookie_re
import cookielib
from setuptools.ssl_support import opener_for
from pip._vendor.requests.packages.urllib3 import response

url="http://www.baidu.com"

print '第一种方法'
response1=urllib2.urlopen(url)#网页下载
print response1.getcode()#打印状态码
print len(response1.read())#打印返回网页内容的长度，read读取长度

print"第二种方法"
request = urllib2.Request(url) 
request.add_header("user-agent","Mozilla/5.0")
response2=urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cj=cookielib.CookieJar()#存储cookie数据
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))#创建容器
urllib2.install_opener(opener)#生成处理器
response3=urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()#输出cookie
