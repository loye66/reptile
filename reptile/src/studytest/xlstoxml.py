#coding:utf8
'''
Created on 2017年5月16日

@author: loye66
'''
import xlrd
import xml.dom.minidom
import os
import json
from xml.dom.minidom import Document


os.chdir(r'E:\pythonwork')
xls=r'student.xls'

#获取xls数据并将其变为可直接输入的数据
def rxls():
    stulst=[]
    rd=xlrd.open_workbook(xls)
    sh=rd.sheet_by_name('test')
    row=sh.nrows
    col=sh.ncols
    rows=map(lambda x: x, sh.get_rows())
    print rows
    for i in range(0,row):
        row_data=sh.row_values(i)
        stulst.append(row_data)
    return stulst

#写入xml文件
def wxml():
    studic=rxls()
    #http://blog.csdn.net/hshl1214/article/details/49124373
    doc = Document()
    #创建一个根节点
    root = doc.createElement('root')
    #根节点插入dom树
    doc.appendChild(root)
    
    #创建子节点student
    student = doc.createElement('student')
    
    for i in studic:
        #指定子节点内容
        n= u'\u738b\u4e94'
        print i[1][0]
        print n.encode('utf-8')
        student_text = doc.createTextNode(str(i))
        #插入数据
        student.appendChild(student_text)
    #加入根节点
    root.appendChild(student)   
    
    with open('student.xml', 'w') as f:
        f.write(doc.toprettyxml(indent='\t', encoding='utf-8'))

if __name__=='__main__':
    wxml()