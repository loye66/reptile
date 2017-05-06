#coding:utf8
'''
Created on 2017年5月4日

@author: loye66
'''
import random
import string
from macpath import join

#创建优惠券列表
list_ActivationCode=[]

#实现获取200优惠券的函数
def get_ActivationCode():
    str=string.letters+string.digits
    for i in range(200):#200次循环
        ActivationCode=''.join(random.sample(str,16))#创建优惠码，使用python join（）方法
        list_ActivationCode.append(ActivationCode)#加入优惠码列表
    print list_ActivationCode,r'\n'
    #分行输出
    for j in range(200):
        print "第",j+1,"个：",list_ActivationCode[j]

if __name__=='__main__':    
      get_ActivationCode()#调取函数