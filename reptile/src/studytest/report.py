# coding:utf-8
from __future__ import division
import xml.dom.minidom
import os
import sys


class CreateReport(object):
    projectName = None

    def __init__(self, projectNames, buildNum):
        self.projectNames = projectNames
        self.buildNum = buildNum
        self.reportTemplatePath = "D:/UiAutomaticTest/reports/reportTemplate/uiAutomatorReportTemplate.html"

    """
    获取xml中需要生成报告的数据
    """

    def get_data_by_xml(self):

        global projectName
        global fileName
        xmlPath = "D:/UiAutomaticTest/reports/%s/output.xml"%self.projectNames
        # 报告生成时间
        xmlDataDic = {}
        dom = xml.dom.minidom.parse(xmlPath)
        root = dom.documentElement
        generated = root.getAttribute("generated")
        xmlDataDic["generated"] = generated

        # 执行开始时间和结束时间
        status = root.getElementsByTagName("status")
        starttime = status[-1].getAttribute("starttime")
        endtime = status[-1].getAttribute("endtime")
        xmlDataDic["starttime"] = starttime
        xmlDataDic["endtime"] = endtime
        fileName = endtime.split(".")[0].strip().replace(":", "-").replace(" ", "--")

        # 用例执行后通过数量和失败数量
        totals = root.getElementsByTagName("total")
        passValue = totals[0].getElementsByTagName("stat")[0].getAttribute("pass")
        failValue = totals[0].getElementsByTagName("stat")[0].getAttribute("fail")
        xmlDataDic["passValue"] = passValue
        xmlDataDic["failValue"] = failValue

        # 项目名称
        projectName = root.getElementsByTagName("suite")[0].getAttribute("source").strip().split("\\")[3]
        xmlDataDic["projectName"] = projectName

        # 计算成功和失败百分值,总数
        intPassValue = int(passValue.encode("utf-8"))
        intFailValue = int(failValue.encode("utf-8"))
        intTotalValue = intPassValue + intFailValue
        passScale = intPassValue / intTotalValue * 100
        failScale = intFailValue / intTotalValue * 100
        xmlDataDic["passScale"] = str(passScale) + "%"
        xmlDataDic["failScale"] = str(failScale) + "%"
        xmlDataDic["intTotalValue"] = intTotalValue

        return xmlDataDic

    def excute_date_to_error_report(self):
        excuteDateToErrorReport = {}
        excuteDateToErrorReport[
            "98"] = "<div  style=\"margin-top: 10px;width:100%;text-align: center; \"  ><h1>" + self.projectNames + "</h1></div>"
        excuteDateToErrorReport["101"] = r"<br>" + "generated"
        excuteDateToErrorReport["113"] = "<td class=\"fail\">" + r"Running failed and needs to run again"
        excuteDateToErrorReport["118"] = "<td>" + "00000000 00:00:00" + "</td>"
        excuteDateToErrorReport["122"] = "<td>" + "00000000 00:00:00" + "</td>"
        excuteDateToErrorReport["172"] = "<td class=\"stats-col-stat\">" + "0" + "</td>"
        excuteDateToErrorReport["173"] = "<td class=\"stats-col-stat\">" + "0" + "</td>"
        excuteDateToErrorReport["174"] = "<td class=\"stats-col-stat\">" + "0" + "</td>"
        return excuteDateToErrorReport

    def excute_date_to_report(self):
        excuteDateToReport = {}
        xmlDataDic = self.get_data_by_xml()
        excuteDateToReport["98"] = "<div  style=\"margin-top: 10px;width:100%;text-align: center; \"  ><h1>" + \
                                   xmlDataDic["projectName"] + "</h1></div>"
        excuteDateToReport["101"] = r"<br>" + xmlDataDic["generated"]
        if int(xmlDataDic["failValue"]) == 0:
            excuteDateToReport["113"] = "<td class=\"pass\">" + r"All tests passed"
        else:
            excuteDateToReport["113"] = "<td class=\"fail\">" + xmlDataDic["failValue"] + r"test failed"
        excuteDateToReport["118"] = "<td>" + xmlDataDic["starttime"] + "</td>"
        excuteDateToReport["122"] = "<td>" + xmlDataDic["endtime"] + "</td>"
        excuteDateToReport["172"] = "<td class=\"stats-col-stat\">" + str(xmlDataDic["intTotalValue"]) + "</td>"
        excuteDateToReport["173"] = "<td class=\"stats-col-stat\">" + xmlDataDic["passValue"] + "</td>"
        excuteDateToReport["174"] = "<td class=\"stats-col-stat\">" + xmlDataDic["failValue"] + "</td>"
        excuteDateToReport["177"] = "<div class=\"pass-bar\" style=\"width: " + xmlDataDic[
            "passScale"] + "\" title=\"" + xmlDataDic["passScale"] + "\"></div>"
        excuteDateToReport["178"] = "<div class=\"fail-bar\" style=\"width: " + xmlDataDic[
            "failScale"] + "\" title=\"" + xmlDataDic["failScale"] + "\"></div>"
        return excuteDateToReport

    def mkdir_cp_report(self):
        linuxReportPath = "\\\\172.30.10.236\\uitestshare\\reports\\" + str(projectName) + "\\" + str(self.buildNum)
        windowsReportPath = "D:\\UiAutomaticTest\\reports\\" + str(projectName) + "\\" + "newReport"
        if os.path.exists(windowsReportPath) == False:
            os.system("md  %s" % windowsReportPath)
        if os.path.exists(linuxReportPath) == False:
            os.system("md  %s" % linuxReportPath)
        os.system("xcopy D:\\UiAutomaticTest\\reports\\%s\\* %s\\" % (projectName, linuxReportPath))
        return linuxReportPath, windowsReportPath

    def create_report(self):
        if os.path.exists("D:\\UiAutomaticTest\\reports\\" + self.projectNames+ "\\" + "log.html") and os.path.exists(
                                        "D:\\UiAutomaticTest\\reports\\" + self.projectNames + "\\" + "report.html"):
            excuteDateToReport = self.excute_date_to_report()
            linuxReportPath, windowsReportPath = self.mkdir_cp_report()
            with open(self.reportTemplatePath, 'r') as readFile:
                readContents = readFile.readlines()

            readContents[97] = excuteDateToReport["98"]
            readContents[100] = excuteDateToReport["101"]
            readContents[112] = excuteDateToReport["113"]
            readContents[117] = excuteDateToReport["118"]
            readContents[121] = excuteDateToReport["122"]
            readContents[171] = excuteDateToReport["172"]
            readContents[172] = excuteDateToReport["173"]
            readContents[173] = excuteDateToReport["174"]
            readContents[176] = excuteDateToReport["177"]
            readContents[177] = excuteDateToReport["178"]
            readContents[182] = "<a href=\"http://172.30.10.236:8002/%s/%s/report.html\">" % (
            projectName, self.buildNum)
            newReportFile = os.path.join(windowsReportPath, "newReport.html")
            with open(newReportFile, "w") as writeContent:
                for readcontent in readContents:
                    writeContent.write(readcontent)
            relist = ["D:\\UiAutomaticTest\\reports\\" + str(projectName) + "\\" + "log.html",
                      "D:\\UiAutomaticTest\\reports\\" + str(projectName) + "\\" + "report.html"]
            for fileName in relist:
                os.remove(fileName)
        else:
            excuteDateToErrorReport = self.excute_date_to_error_report()
            windowsReportPath1 = "D:\\UiAutomaticTest\\reports\\" + self.projectNames + "\\" + "newReport"
            with open(self.reportTemplatePath, 'r') as readFile:
                readContents = readFile.readlines()

            readContents[97] = excuteDateToErrorReport["98"]
            readContents[100] = excuteDateToErrorReport["101"]
            readContents[112] = excuteDateToErrorReport["113"]
            readContents[117] = excuteDateToErrorReport["118"]
            readContents[121] = excuteDateToErrorReport["122"]
            readContents[171] = excuteDateToErrorReport["172"]
            readContents[172] = excuteDateToErrorReport["173"]
            readContents[173] = excuteDateToErrorReport["174"]
            newReportFile = os.path.join(windowsReportPath1, "newReport.html")
            with open(newReportFile, "w") as writeContent:
                for readcontent in readContents:
                    writeContent.write(readcontent)


if __name__ == '__main__':
    projectNames = sys.argv[1]
    buildNum = sys.argv[2]
    createreport = CreateReport(projectNames, buildNum)
    createreport.create_report()
