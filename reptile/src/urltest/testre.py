#coding:utf8
'''
Created on 2017年4月24日

@author: loye66
'''
import re
r1=re.compile(r'world')
if r1.match('helloworld'):
    print 'match succeeds'
else:
    print 'match fails'#从第一个位置开始匹配

if r1.search('helloworld'):
    print 'search succeeds'
else:
    print 'search fails'#整个字符串搜索
    
if re.search(r'abc','helloaaabcdworldn'):
    print 'search succeeds'
else:
    print 'search fails'
    
r2=re.compile('\W+')
print r2.split('192.168.1.1')
print re.split('(\W+)','192.168.1.1')
print re.split('(\W+)','192.168.1.1',1)

r3=re.compile('([i*])')
print re.findall(r3,"hello[hi]heldfsdsf[iwonder]lo")
r4=re.compile('([.*?])')
print re.findall(r4,"hello[hi.]heldfsdsf[iwonder]lo")
print re.findall('[0-9]{2}',"fdskfj1323jfdj")
print re.findall('([0-9][a-z])',"fdskj1323jfkdj")
print re.findall('(?=www)',"afdsfwwwfkdifsdfsdwww")
print re.findall('',"afdsfwwwfkdjfsdfsdwww")

p = re.compile('...')
m = p.match( 'string goes here' )
if m:
    print 'Match found: ', m.group()
else:
    print 'No match'

import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) (.*).*', line, re.M|re.I)

if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(3) : ", searchObj.group(3)
else:
   print "Nothing found!!"

'''s = 'good work, man!'
ss=s.split('good work')
t=type(ss)
if t==list:
  print("ss is :")
  print(ss)
  print("ss type is list")'''
