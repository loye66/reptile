#coding:utf8
'''
Created on 2017年4月26日

@author: loye66
'''
import os
from robot.utils.asserts import fail
import re
from wxPython._wx import NULL

print "培训ppt实例1：-----------------------------------"
os.chdir(r"E:\pythonwork")
f=open("list.dat",'r+')#读dat文件
f1=f.readlines()#获取dat数据
f2=f1[1].split(' ')#将字符串按空格分割变未为list
f3=f1[2].split(' ')
f4=f1[3].split(' ')
f5=f1[4].split(' ')
name=[f2[0],f3[0],f4[0],f5[0]]#或去每一行该列数据为一个list
age=[f2[1],f3[1],f4[1],f5[1]]
level=[f2[2],f3[2],f4[2],f5[2]]
count=0#用于计数
sum=0
while True:
    if age[count]>sum:#找出最大
        sum=age[count]
    count=count+1
    if count==3:
        break#退出去循环
print "年龄最大=",sum
for a in range(0,3):
    if sum==age[a]:
        print "a=",a
        break#找出最大值对应的行
print "name =",name[a],"\nage =",age[a],"\nlevel =",level[a]

print "培训ppt实例2：------------------------------------"
os.chdir(r"E:\pythonwork")
os.getcwd()
fp=open("shili2.txt","r")#读取文件
fx=fp.readlines()
print fx
fp.close()
r1=re.compile(r'inet addr')
fn=''
for i in range(len(fx)):
    if r1.match(fx[i]):
        fn=fn+fx[i]
        print fn
fm=open('temp.bak','w+')
fm.writelines(fn)
fm=open('temp.bak','r')
fs=fm.readlines()
print fs
fm.close()
        




        
    
    