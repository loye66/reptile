#coding:utf8
'''
Created on 2017年4月26日

@author: loye66
'''
import os
import re

print "培训ppt实例2：------------------------------------"
os.chdir(r"E:\pythonwork")

#判断文件是不是txt或者log
def judgetxt(txtname):
    r2=re.compile(r'.log')
    r3=re.compile(r'.txt')
    if r2.search(txtname):
        return 1
    elif r3.search(txtname):
        return 2
    else:
        return 3

#遍历并读取文件    
def readtxt():
    loglst=[]
    fs=[]  
    for roots, dirs, files in os.walk(r"E:\pythonwork"):
        for file in files:
            txt=os.path.join(roots, file)#txt=目录+文档名
            loglst.append(txt)#讲txt转换为list
            
    for j in loglst:
        if judgetxt(j)==1 or judgetxt(j)==2:
            fp=open(j,"r")#读取文件
            fx=fp.readlines()
            fs=fs+fx
            fp.close()           
        #else:
            #print j,'：该文件不是TXT或者log' #不是txt和log文件时，输出可注释
    return fs

#写入文件  
def writetemp():
    fx=readtxt() 
    r1=re.compile(r'inet addr')
    fn=''
    for i in fx:
        if r1.match(i):
            fn=fn+i
            #print fn
    fm=open('temp.bak','w+')
    fm.writelines(fn)
    fm=open('temp.bak','r')
    fs=fm.readlines()
    print fs
    fm.close()
    
#主函数       
if __name__=='__main__':
    writetemp()



        
    
    