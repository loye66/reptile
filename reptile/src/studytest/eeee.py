# -*- coding: utf-8 -*-
import xlrd
from xml.dom import minidom
from xml.dom.minidom import getDOMImplementation
import  os


class ImportTestCaseToTestLink(object):
    def __init__(self, excel_file, xml_file):
        self.wb_obj = xlrd.open_workbook(excel_file)
        self.tree = minidom.parse(xml_file)
        self.xml_file = xml_file

    def getCasesInfo(self):
        for sheet in self.wb_obj.sheets():
            first_row_values = sheet.row_values(0)#获取excel第一排数据
            if (u"用例编号" and u"用例标题(Title)" and u"前置条件(pre-condition)" and u"操作步骤（steps）" and u"预期结果（expection result）") in first_row_values:
                #分别将每一列定位各自索引，对象实例化
                #caseID_index = first_row_values.index(u"用例编号")
                summary_index = first_row_values.index(u"用例标题(Title)")
                preconditions_index = first_row_values.index(u"前置条件(pre-condition)")
                actions_index = first_row_values.index(u"操作步骤（steps）")
                expectedResult_index = first_row_values.index(u"预期结果（expection result）")
                #map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
                #将sheet,get_rows抽取一行数据，并用map将其变为一个序列
                rows = map(lambda x: x, sheet.get_rows())
                #得到用例信息
                if len(rows) > 1:
                    casesInfo = []
                    for row in rows[1:]:
                        caseInfo = {}
                        #分别获取summary precondition expected_result action的数据
                        #caseInfo["caseID"] = row[caseID_index].value
                        caseInfo["summary"] = row[summary_index].value
                        caseInfo["caseName"] = row[summary_index].value#+"+"+row[caseID_index].value
                        caseInfo["preconditions"] = row[preconditions_index].value
                        expected_results = row[expectedResult_index].value
                        # if "\n" not in expected_results.strip():
                        #     caseInfo["expected_result"] = expected_results
                        #     caseInfo["action"] = row[actions_index].value
                        caseInfo["expected_result"] = expected_results#疑问：为什么不直接caseInfo["expected_result"]=row[expectedResult_index].value
                        caseInfo["action"] = row[actions_index].value
                        # else:
                        #     print expected_results.strip()
                        #     expected_result = expected_results.strip().split("\n")
                        #     action = row[actions_index].value.strip().split("\n")
                        #     count = 0
                        #     while count < len(expected_result):
                        #         caseInfo["action{}".format(count + 1)] = action[count]
                        #         caseInfo["expected_result{}".format(count + 1)] = expected_result[count]
                        #         count += 1
                        casesInfo.append(caseInfo)
                    #返回用例数据列表
                    return casesInfo

    def generate_child_node(self, casesInfo):
        childElements = []
        for caseInfo in casesInfo:
            print "start"
            baseElement = self.tree.createElement("testcase")
            baseElement.setAttribute("name", caseInfo["caseName"])
            print caseInfo["caseName"]
            node_order_element = self.tree.createElement("node_order")
            baseElement.appendChild(node_order_element)
            externalid_element = self.tree.createElement("externalid")
            baseElement.appendChild(externalid_element)
            version_element = self.tree.createElement("version")
            baseElement.appendChild(version_element)
            summary_element= self.tree.createElement("summary")
            #summary_element.nodeValue = "<![CDATA[<p>" + caseInfo["summary"] + "</p>"
            baseElement.appendChild(summary_element)
            preconditions_element = self.tree.createElement("preconditions")
            #preconditions_element.nodeValue = '{}caseInfo["preconditions"]{}'.format("![CDATA[<p>", "</p>]]")
            baseElement.appendChild(preconditions_element)
            execution_type_element = self.tree.createElement("execution_type")
            baseElement.appendChild(execution_type_element)
            importance_element = self.tree.createElement("importance")
            baseElement.appendChild(importance_element)
            estimated_exec_duration_element = self.tree.createElement("estimated_exec_duration")
            baseElement.appendChild(estimated_exec_duration_element)
            status_element = self.tree.createElement("status")
            baseElement.appendChild(status_element)
            is_open_element = self.tree.createElement("is_open")
            baseElement.appendChild(is_open_element)
            active_element = self.tree.createElement("active")
            baseElement.appendChild(active_element)
            print 1
            steps_element = self.tree.createElement("steps")
            step_element = self.tree.createElement("step")
            step_number_element = self.tree.createElement("step_number")
            # step_number_element.nodeValue = "<![CDATA[1]]>"
            step_element.appendChild(step_number_element)
            print 2
            actions_element = self.tree.createElement("actions")
            #actions_element.nodeValue = "<![CDATA[<p>" + caseInfo["action"] + "</p>"
            step_element.appendChild(actions_element)
            print 3
            expected_results_element = self.tree.createElement("expectedresults")
            #expected_results_element.nodeValue = "<![CDATA[<p>" + caseInfo["expected_result"] + "</p>"
            step_element.appendChild(expected_results_element)
            execution_type_element = self.tree.createElement("execution_type")
            #expected_results_element.nodeValue = "<![CDATA[<p>" + caseInfo["expected_result"] + "</p>"
            step_element.appendChild(execution_type_element)
            print 4
            steps_element.appendChild(step_element)
            print 5
            baseElement.appendChild(steps_element)
            print 6
            childElements.append(baseElement)
        return childElements

    def replace_node_value(self, element,summary,preconditons, actions, expectedresults, externalid):#从模板中获得一些固定数据
        # element.getElementsByTagName("node_order")[0].appendChild(self.tree.createTextNode("test").replaceWholeText(
        #     '<![CDATA[1000]]>'))
        element.getElementsByTagName("node_order")[0].appendChild(self.tree.createCDATASection("1000"))
        element.getElementsByTagName("externalid")[0].appendChild(self.tree.createCDATASection(externalid))
        element.getElementsByTagName("version")[0].appendChild(self.tree.createCDATASection("1"))
        p_element = self.tree.createElement("p")
        element.getElementsByTagName("summary")[0].appendChild(p_element.appendChild(self.tree.createCDATASection("<p>" + summary + "</p>")))
        element.getElementsByTagName("preconditions")[0].appendChild(p_element.appendChild(self.tree.createCDATASection("<p>" + preconditons + "</p>")))
        element.getElementsByTagName("importance")[0].appendChild(self.tree.createCDATASection("2"))
        element.getElementsByTagName("status")[0].appendChild(self.tree.createTextNode("test").replaceWholeText(
            '1'))
        element.getElementsByTagName("is_open")[0].appendChild(self.tree.createTextNode("test").replaceWholeText(
            '1'))
        element.getElementsByTagName("active")[0].appendChild(self.tree.createTextNode("test").replaceWholeText(
            '1'))
        element.getElementsByTagName("actions")[0].appendChild(
            p_element.appendChild(self.tree.createCDATASection("<p>" + actions + "</p>")))
        element.getElementsByTagName("expectedresults")[0].appendChild(
            p_element.appendChild(self.tree.createCDATASection("<p>" + expectedresults + "</p>")))
        element.getElementsByTagName("step_number")[0].appendChild(self.tree.createCDATASection("1"))
        element.getElementsByTagName("execution_type")[0].appendChild(self.tree.createCDATASection("1"))
        element.getElementsByTagName("execution_type")[1].appendChild(self.tree.createCDATASection("1"))

    def save_xml(self):
        f = open("DPQ.xml", "w")
        f.write(self.tree.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
        f.close()

    def get_max_externalid(self):
        max_externalid = int(max(map(lambda x: x.firstChild.nodeValue, filter(lambda x: x.firstChild, self.tree.getElementsByTagName("externalid")))))
        return max_externalid

    def main(self):
        casesInfo = self.getCasesInfo()#[:3]
        childNodes = self.generate_child_node(casesInfo)
        for childNode in childNodes:
            self.tree.getElementsByTagName("testsuite")[0].appendChild(childNode)
        max_externalid = self.get_max_externalid()
        for element in self.tree.getElementsByTagName("testcase"):
            caseName = element.getAttribute("name")
            if caseName in map(lambda x: x["caseName"], casesInfo):#map+匿名将所有casename变为一个列表
                caseInfo = filter(lambda x: x["summary"] == caseName, casesInfo)[0]
                self.replace_node_value(element,caseInfo["summary"],caseInfo["preconditions"], caseInfo["action"], caseInfo["expected_result"], str(max_externalid + 1))
                print max_externalid
                max_externalid += 1
        # print self.tree.toxml()
        self.save_xml()

if __name__ == '__main__':
    os.chdir(r'D:\testingxml')
    ImportTestCaseToTestLink = ImportTestCaseToTestLink("DPQ.xlsx", "test.xml")
    ImportTestCaseToTestLink.main()
