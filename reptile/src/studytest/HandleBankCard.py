#coding:utf8
'''
create by liuyaqing
create date 2017/08/16
用于:隐藏银行卡中间的数据
'''

import os
import xlrd
from xlutils.copy import copy

class HandleBankCard(object):
    def __init__(self, excel_file):
        self.wb_obj = xlrd.open_workbook(excel_file)

#获取序号，银行卡号
    def getInfo(self):
        for sheet in self.wb_obj.sheets():
            first_row_values = sheet.row_values(0)#获取excel第一排数据
            if (u"序号" and u"银行卡号" ) in first_row_values:
                ordnum_index = first_row_values.index(u"序号")
                mknum_index = first_row_values.index(u"银行卡号")
                rows = map(lambda x: x, sheet.get_rows())
                if len(rows) > 1:
                    marksInfo = []
                    for row in rows[1:]:
                        markInfo = {}
                        markInfo["ordnum"] = int(row[ordnum_index].value)
                        markInfo["BCnum"] = int(row[mknum_index].value)
                        marksInfo.append(markInfo)
                    return marksInfo

    def main(self):
        w = copy(self.wb_obj)
        sh = w.get_sheet(0)
        marksInfo = self.getInfo()
        for markInfo in marksInfo:
            #print type(markInfo["BCnum"])
            BCstr = str(markInfo["BCnum"])
            l = len(BCstr) - 4
            # print  l
            q4 = BCstr[0:4]
            h4 = BCstr[l:len(BCstr)]
            BCstr2 = ""
            for i in range(len(BCstr) - 8):
                print i
                BCstr2 = BCstr2 + "*"
            sh.write(markInfo["ordnum"],12,q4+BCstr2+h4)#字符串不可改，只能重新生成新的字符串
        w.save(u'全国分组测试(处理后).xls')

if __name__=='__main__':
    os.chdir(r"E:\pythonwork")
    HandleBankCard=HandleBankCard(u"全国分组测试.xlsx")
    HandleBankCard.main()