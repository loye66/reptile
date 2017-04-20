#coding:utf8
'''
Created on 2017年4月20日

@author: loye66
'''
from pip._vendor.distlib.locators import HTML_CONTENT_TYPE
from urltest.testbs4 import soup
from bs4 import BeautifulSoup


class HtmlParser(object):
    
    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup =BeautifulSoup()
    
    
    
    



