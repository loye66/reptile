# -*- coding: utf-8 -*-
'''
Created on 2017年5月12日

@author: loye66
'''
import xlrd
import xlwt
import os
import re
import json
import codecs

os.chdir(r'E:\pythonwork')

#获取txt中的数据并抽取
def getdata():
    stu=[]
    with open(r'student.txt') as fp:
        fx = fp.readlines()       
        r1=re.compile(r'"([0-9])"')
        for i in fx:
            if r1.search(i):
                #strip去掉开头的空格，然后用replace去掉多余的符号
                n=i.strip(' ').replace(':',',').replace('[','').replace(']','').replace('"','')
                stu.append(n.split(','))
        print stu[0]   
    return stu
#写入xls，并读取文件
def writedata():      
    stu=getdata()
    wb = xlwt.Workbook(encoding='gbk')
    sheet = wb.add_sheet('test')#sheet的名称为test    
    stu1=list(stu)
    print stu1
    #python enumerate用于遍历序列中的元素以及它们的下标
    for i in range(0,len(stu1)):
        for j in range(0,len(stu1[i])):
            print stu1[i][j]
            sheet.write(i, j, stu1[i][j])
    wb.save('student.xls')
    
    
if __name__=='__main__':
    writedata()