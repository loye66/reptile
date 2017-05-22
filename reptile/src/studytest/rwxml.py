#coding:utf8
'''
Created on 2017年5月15日

@author: loye66
'''

import xml.dom.minidom

dom=xml.dom.minidom.parse(r'E:\pythonwork\movie.xml')

#获取element collection 和它的属性（Attribute属性）
collection=dom.documentElement
if collection.hasAttribute('shelf'):
    print 'shelf = %s'%collection.getAttribute('shelf')

movies=dom.getElementsByTagName('movie')
print movies

for movie in movies:
    print '--------------------------------------'
    #获取title并输出
    if movie.hasAttribute('title'):
        print 'title = %s'%movie.getAttribute('title')
    type=movie.getElementsByTagName("type")[0]
    print 'type = %s'%type.childNodes[0].data
    format=movie.getElementsByTagName('format')[0]
    print 'format = %s'%format.childNodes[0].nodeValue#也可以用nodeValue获取数据
   # episodes=movie.getElementsByTagName('episodes')[0]
    #print 'episodes = %s'%episodes.childNodes[0].data
    rating=movie.getElementsByTagName('rating')[0]
    print 'rating = %s'%rating.childNodes[0].data
    stars=movie.getElementsByTagName('stars')[0]
    print 'stars = %s'%stars.childNodes[0].data
    description=movie.getElementsByTagName('description')[0]
    print 'description = %s'%description.childNodes[0].data
    