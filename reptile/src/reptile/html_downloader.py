#coding:utf8
'''
Created on 2017年4月20日

@author: loye66
'''
import urllib2
from pip._vendor.requests.packages.urllib3 import response


class Htmldownloader(object):
       
    def download(self,url):
        if url is None:
            return None
        response=urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        return response.read()
        
    
    
    
    



