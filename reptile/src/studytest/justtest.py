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
for i in range(0,len(rowlst)):
    for j in range(0,len(row_data)):
        print rowlst[i][j]


class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for i in range(num/2):
            L.append(a)
            L.append(b)
            a = a + b
            b = a + b
        self.numbers = L
    def __str__(self):
        return str(self.numbers)


    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)
