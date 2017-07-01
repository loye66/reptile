#coding:utf8
'''
Created on 2017年5月23日

@author: loye66
'''
import xlrd
import xml.dom.minidom
import os
import json
from xml.dom.minidom import Document

os.chdir(r'E:\pythonwork')

def readcase():
    rd = xlrd.open_workbook(r'迁移分类测试用例.xlsx')
    sh = rd.sheet_by_name('Sheet1')




def toxml():
    return 0

import time

def performance(unit):
    def per(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit=='ms':
                print 'call %s() in %f ms' % (f.__name__, ((t2 - t1)*1000))
            else:
                print 'call %s() in %fs' % (f.__name__, (t2 - t1))
            return r
        return fn
    return per

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))


if __name__=='__main__':
    print factorial(10)
