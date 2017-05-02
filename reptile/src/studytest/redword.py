#coding:utf8
'''
Created on 2017年4月30日

@author: loye66
'''
from PIL import Image,ImageDraw,ImageFont
from email.mime import image
import os

#切换到工作目录
os.chdir(r"E:\pythonwork")
os.remove("susu2.png")
#os.remove("susu3.png")

#图片地址
imagepath=r"E:\pythonwork"

#采用字体
font=ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf", 40)

#打开图片
im=Image.open('susu.png')

#打开画布指定大小输出
draw=ImageDraw.Draw(im)
draw.text((234,30),'4',(255,0,0) , font=font)
draw=ImageDraw.Draw(im)
im1="susu2.png"
im.save(im1)
print '图片另存为:',imagepath+'\\'+im1

#初始化图片
im.close()
im=Image.open('susu.png')

#根据图片大小自动输出
fontsize=min(im.size)/4
draw=ImageDraw.Draw(im)
fontobj=ImageFont.truetype(r"C:\Windows\Fonts\Arial.ttf",size=fontsize)#实例字体对象
draw.text((im.size[0]-fontsize,0),text="4",fill=(255,0,0),font=fontobj)
draw=ImageDraw.Draw(im)
im2="susu3.png"
im.save(im2)
print '图片另存为:',imagepath+'\\'+im2




