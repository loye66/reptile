#coding:utf8
'''
Created on 2017年5月4日

@author: loye66
'''
import MySQLdb as mdb#mysqldb变为mdb
import random
import string
from macpath import join

#将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中

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
        
def insertdata():
    get_ActivationCode()#调用get_ActivationCode()
    try:  
        #链接数据库并实例化
        con=mdb.connect('localhost','root','123456','test')    
        #获取连接的 游标，只有获取了 cursor，我们才能进行各种操作
        cur=con.cursor()
        #选中数据库
        con.select_db('test')
        #删除表ActivationCode
        cur.execute("DROP TABLE IF EXISTS ActivationCode")
        #创建新表    
        cur.execute("create table ActivationCode(id int,code varchar(50))")
        #插入数据
        for m in range(len(list_ActivationCode)):
            cur.execute('insert into ActivationCode values(%s,%s)',(m,list_ActivationCode[m]))
        n=cur.execute("select*from ActivationCode")
        print n
        #提交到数据库执行
        con.commit()
        #关闭游标
        cur.close()
    except:
        #发生错误回滚
        con.rollback()
    #关闭数据库链接        
    con.close()
        
if __name__=='__main__':  
    insertdata()


