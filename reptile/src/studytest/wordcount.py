#coding:utf-8
'''
Created on 2017年5月6日

@author: loye66
'''
import re
import os

#任一个英文的纯文本文件，统计其中的单词出现的个数

def wordcount():
    #打开文件获得数据
    os.chdir(r"E:\pythonwork")
    #打开文档
    fp=open('outofthewoods.txt','r+')
    #读取文档数据
    f1=fp.readlines()
    print f1
    #获取待查询数据
    word=raw_input("请输入要查询的单词：")   
    s=''.join(word)
    #设置对比
    r1=re.compile(s)
    count=0#计数
    #查询数据
    for i in range(len(f1)):
        if r1.search(f1[i].lower()):#注意全部变为小写或者大写在进行对比
            count=count+1
    return count

if __name__=='__main__': 
    print wordcount()