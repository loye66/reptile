#coding:utf-8
'''
Created on 2017年4月19日

@author: liuyaqing
'''
from bs4 import BeautifulSoup
from pip.index import Link
from setuptools.package_index import HREF
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup=BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print '获取所有的链接'
links=soup.find_all('a')
for link in  links :
    print link.name,link['href'],link.get_text()
    
print'获取lacie的链接'
link_node=soup.find('a',href='http://example.com/lacie')
print link_node.name,link_node['href'],link_node.get_text()

print '正则匹配'
link_node=soup.find('a', href=re.compile(r"ill"))
print link_node.name,link_node['href'],link_node.get_text()

print '获取P段落文章'
p_123=soup.find('p',class_="title")
print p_123.name,p_123.get_text()
