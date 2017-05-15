#coding:utf8
import xlwt
import os
import xlrd

os.chdir(r'E:\pythonwork')
#写入xls
w = xlwt.Workbook(encoding='utf8')  #创建一个工作簿
ws = w.add_sheet('Hey, Hades')  #创建一个工作表
lst=[['我','huang','xuan'],[60,90,70]]
for i in range(len(lst)):
    for j in range(len(lst[i])):
        ws.write(i,j,lst[i][j])   
w.save('mini.xlsx')  #保存

#读取xls
rowlst=[]
rad=xlrd.open_workbook('mini.xlsx')
sh=rad.sheet_by_name('Hey, Hades')
row=sh.nrows
col=sh.ncols
print row,col
for m in range(0,row):
    row_data=sh.row_values(m)
    rowlst.append(row_data)
print rowlst



    