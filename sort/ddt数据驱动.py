# 1.创建字典数据
# 2.导入ddt模块
# 3.用ddt修饰，注解unittest类
# 4.使用data修饰测试用例
# 5.重写声明测试用例名称，test_very_01(self,para)
# 6.使用para["username"]


# ###############案例一

from selenium import webdriver
import time
import unittest
from ddt import ddt,data

# 使用字典数据结构存储数据，实现数据驱动
# dictvalue = [{'username':"aaaaa","email":"222222@163.com","password":"123456","repassword":'123456'},
#            {'username':"bbbbb","email":"333333@163.com","password":"123456","repassword":'123456'},
#            {'username':"ccccc","email":"444444@163.com","password":"123456","repassword":'123456'}]
#
# @ddt
# class ddt_value(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     @data(*dictvalue)
#     def test_very_01(self,para):
#         driver = webdriver.Chrome()
#         driver.get('')
#
#         driver.find_element_by_link_text('免费注册').click()
#         driver.find_element_by_id('username').send_keys(para["username"])     #循环输入dictvar中的username数据
#         driver.find_element_by_id('email').send_keys(para['email'])           #循环输入dictvar中的email数据
#         driver.find_element_by_id('password').send_keys(para['password'])     #循环输入dictvar中的password数据
#         driver.find_element_by_id('repassword').send_keys(para['repassword'])  #循环输入dictvar中的repassword数据
#
#         time.sleep(3)
#         expecturl = ''        #拿到注册成功页面的url地址
#         actvalue = driver.current_url      #拿到当前页面的url
#
#         if expecturl==actvalue:
#             print("注册的正向测试用例通过")
#         else:
#             print('注册的正向测试用例不通过')
#         driver.quit()
#     def tearDown(self):
#         pass


# ###########方式二
import xlrd
import os

paths = os.path.dirname(os.path.dirname(__file__))+r"/sort/execl_001.xlsx"
datas = xlrd.open_workbook(paths)
table = datas.sheets()[0]
value1 = table.row_values(1)
value2 = table.col_values(0)

nrow = table.nrows    # 有多少行数据
ncol = table.ncols    # 有多少列数据

for i in range(nrow):
    for j in range(ncol):
        print(table.cell(i,j).value)