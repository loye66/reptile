#coding=utf8
'''
Created on 2017年5月6日

@author: loye66
'''
#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
import re
from studytest.redword import draw
from PIL import Image,ImageDraw

#图片大小辨别
def judgeimg(im):   
    (x,y)=im.size
    if x>1136 and y<640:
        return 1
    elif x<1136 and y>640:
        return 2
    elif x>1136 and y>640:
        if 1136/x > 640/y:
            return 3
        if 1136/x < 640/y:
            return 4
    else:
        return 5

    #循环遍历处理超过大小的图片
def main():
    #定义图片路径
    imgpath = r"E:\pythonwork\manyimg"  
    #需要切换工作目录，否则找不到文件
    os.chdir(r"E:\pythonwork\manyimg")  
    #os.listdir获取路径里面的文件的文件名并变为一个list
    imgslst =  os.listdir(imgpath)
    for i in imgslst:
        im=Image.open(i)
        if judgeimg(im)==1:#被调用的函数要排在前面
            (x,y)=im.size
            x_s=1136
            y_s=int((1136/float(x))*y)#1136/x是小数,不强制转换会变0
            out = im.resize((x_s,y_s),Image.ANTIALIAS)#Image.ANTIALIAS平滑除锯齿生成图片
            out.save(i)
            print i,'oldsize:',x,y,'newsize:',x_s,y_s
        elif judgeimg(im)==2:
            draw=ImageDraw.Draw(im)
            (x,y)=im.size
            y_s=640
            x_s=int((640/float(y))*x)            
            out = im.resize((x_s,y_s),Image.ANTIALIAS)
            out.save(i)
            print i,'oldsize:',x,y,'newsize:',x_s,y_s
        elif judgeimg(im)==3:
            draw=ImageDraw.Draw(im)
            (x,y)=im.size
            x_s=1136
            y_s=int((1136/float(x))*y)         
            out = im.resize((x_s,y_s),Image.ANTIALIAS)
            out.save(i)
            print i,'oldsize:',x,y,'newsize:',x_s,y_s
        elif judgeimg(im)==4:
            draw=ImageDraw.Draw(im)
            (x,y)=im.size
            y_s=640
            x_s=int((640/float(y))*x)  
            out = im.resize((x_s,y_s),Image.ANTIALIAS)
            out.save(i)
            print i,'oldsize:',x,y,'newsize:',x_s,y_s
        else:
            print i,"本身小于苹果5的分辨率，不需要处理"
    
if __name__=="__main__":
    main()   
    

    


