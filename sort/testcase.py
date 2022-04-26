# 高聚能，低耦合
"""
自动化测试的主要步骤：
1.通过某些方式定位到我们要执行的对象，目标
2.对这个对象进行什么操作
3.通过操作对定位到的元素赋值
4.添加断言操作

在编写自动化测试用例过程中应该遵循以下原则:
1.一个用例为一个完整的场景，从用户登录系统到最终退出并关闭浏览器。
2.一个用例只验证一个功能点，不要试图在用户登录后把所有的功能都验证一遍。
3.尽可能少的编写逆向测试用例。一方面因为逆向逻辑的用例很多（例如，手机号输错有几十种情况另一方面自动化测试脚本本身比较脆弱，
复杂的逆向逻辑用例实现起来较为麻烦且容易出错。)
4.用例和用例之间尽量避免产生依赖。[
5.一条用例完成测试之后需要对测试场景进行还原，以免影响其它用例的执行。

测试点转为测试用例的原则是什么?
设计─条正向用例，覆盖足够多的有效等价类数据
设计一条反向用例，需要覆盖一条无效等价类数据

"""


# ######################自动化脚本开发

"""
线性测试：最基本的代码组织形式，存粹是模拟用户步骤或者场景
        1.维护性比较差
        2.模块比较多，运行起来比较麻烦，写一个额外的模块作为主运行模块
        3.如果所有用例的步骤放在一个模块，可读性非常差
        4.脚本给出的结果不一定是bug

模块化驱动测试:
把常用、公用的一些功能、业务、步骤专门提取出来，写在一个专门的模块中，
以方法、类的形式实现出来，再其他的模块如果需要这些功能，直接调用即可，
无需重复显示这些代码。比如可以做登录模块、退出模块、邮件发送模块、数据库处理模块、日志生成模块等
模块化驱动测试最大层度地去除了重复，提高了测试脚本的复用性和可维护性。|


"""

# from selenium import webdriver
# import time
# class very_login():
#     def __init__(self):                           #创建浏览器对象
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(10)             #隐性等待10秒
#         self.driver.get('https://www.qq.com/')      #输入qq网址
#     def login(self):
#         self.driver.find_element_by_link_text('登录').click()    #点击登录按钮
#         self.driver.switch_to.frame('ptlogin_iframe')           #绑定页面frame表单
#         self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()        #点击账号密码登录
#         self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('2478206298')        #输入账号
#         self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('cheng17370091167')   #输入密码
#         self.driver.find_element_by_xpath('//*[@id="login_button"]').click()       #点击登录
#         time.sleep(3)
#     def logout(self):
#         aa = self.driver.find_element_by_xpath('//*[@id="userPic_s"]')
#         ctionChains(self.driver).move_to_element(aa).perform()
#         self.driver.find_element_by_xpath('//*[@id="top-login"]/div[3]/div/a').click()
#
#     def quitA(self):            #定义退出浏览器对象
#         self.driver.quit()
#
# if __name__ == '__main__':
#      ss = very_login()            #创建实例
#      ss.login()
#      ss.logout()
#      ss.quitA()


# ####################另一种方法
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# class very_login():
#     def login(self,driver):
#         self.driver = driver
#         self.driver.implicitly_wait(10)        # 隐性等待10秒
#         self.driver.get('https://www.qq.com/')
#         self.driver.find_element_by_link_text('登录').click()    #点击登录按钮
#         self.driver.switch_to.frame('ptlogin_iframe')           #绑定页面frame表单
#         self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()        #点击账号密码登录
#         self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('2478206298')        #输入账号
#         self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('cheng17370091167')   #输入密码
#         self.driver.find_element_by_xpath('//*[@id="login_button"]').click()       #点击登录
#         time.sleep(3)
#
#     def logout(self,driver):                     #退出登录
#         self.driver = driver
#         aa = self.driver.find_element_by_xpath('//*[@id="userPic_s"]')    #悬停头像
#         ActionChains(self.driver).move_to_element(aa).perform()
#         self.driver.find_element_by_xpath('//*[@id="top-login"]/div[3]/div/a').click()   #点击退出登录
#
#
#     def quitA(self,driver):            #定义退出浏览器对象
#         self.driver = driver
#         self.driver.quit()
#
# if __name__ == '__main__':
#      driver = webdriver.Chrome()
#      ss = very_login()            #创建实例
#      ss.login(driver)
#      ss.logout(driver)
#      ss.quitA(driver)



"""
数据驱动测试：
由数据的改变驱动测试的执行，最终改变测试结果，这种方式就是数据驱动测试
数据的存储：
1.字典
2.csv文件
3.execl文件

"""
from selenium import webdriver
import time

# 定义字典数据，用来存储注册数据的（用户名，email，密码，确认密码，断言）
# 字典中存在数据，字典放列表
# 如果你的数据不合理，用例的执行结果是错的

# ################# 正向测试用例
# dictvar = [{'username':"aaaaa","email":"222222@163.com","password":"123456","repassword":'123456'},
#            {'username':"bbbbb","email":"333333@163.com","password":"123456","repassword":'123456'},
#            {'username':"ccccc","email":"444444@163.com","password":"123456","repassword":'123456'}]
#
# for i in dictvar:
#     driver = webdriver.Chrome()
#     driver.get('')
#
#     driver.find_element_by_link_text('免费注册').click()
#     driver.find_element_by_id('username').send_keys(i["username"])     #循环输入dictvar中的username数据
#     driver.find_element_by_id('email').send_keys(i['email'])           #循环输入dictvar中的email数据
#     driver.find_element_by_id('password').send_keys(i['password'])     #循环输入dictvar中的password数据
#     driver.find_element_by_id('repassword').send_keys(i['repassword'])  #循环输入dictvar中的repassword数据
#
#     time.sleep(3)
#     expecturl = ''        #拿到注册成功页面的url地址
#     actvalue = driver.current_url      #拿到当前页面的url
#
#     if expecturl==actvalue:
#         print("注册的正向测试用例通过")
#     else:
#         print('注册的正向测试用例不通过')
# driver.quit()


# ################# 反向测试用例
# dictvar = [{'username':"aaaaa","email":"222222@163.com","password":"123456","repassword":'123456','expect':'空'},
#            {'username':"bbbbb","email":"333333@163.com","password":"123456","repassword":'123456','expect':'字数过少'},
#            {'username':"ccccc","email":"444444@163.com","password":"123456","repassword":'123456','expect':'字数过多'}]
#
# for i in dictvar:
#     driver = webdriver.Chrome()
#     driver.get('')
#
#     driver.find_element_by_link_text('免费注册').click()
#     driver.find_element_by_id('username').send_keys(i["username"])     #循环输入dictvar中的username数据
#     driver.find_element_by_id('email').send_keys(i['email'])           #循环输入dictvar中的email数据
#     driver.find_element_by_id('password').send_keys(i['password'])     #循环输入dictvar中的password数据
#     driver.find_element_by_id('repassword').send_keys(i['repassword'])  #循环输入dictvar中的repassword数据
#
#     expect = i['expect']                #循环输入dictvar中的expect数据
#     actvalue = driver.find_element_by_xpath('')     #定位到注册失败的提示信息
#
#     if expect==actvalue:
#         print("注册的反向测试用例通过")
#     else:
#         print('注册的反向测试用例不通过')
# driver.quit()



""""
csv文件的创建：
1.创建一个execl文件，录入数据
2.将execl文件另存为utf—8格式的带逗号分隔符的csv文件
3.使用notepad记事本文件将csv文件转码为utf—8
如何读取csv文件中的数据：
with open(r"./excsv.csv","r",encoding="utf-8") as f:
    data = csv.reader(f)

os.path.dirname(__file__)    获取当前编辑文件的目录
"""
# from selenium import webdriver
# import time
# import csv
# import os
# #filename = os.path.dirname(__file__)+r"/excsv.csv"           #好处：不会因为你的文件移动位置而导致报错
# #with open(filename,"r",encoding="utf-8") as f:

# with open(r"./excsv.csv","r",encoding="utf-8") as f:
#     data = csv.reader(f)
#     for i in data:
#         driver = webdriver.Chrome()
#         driver.get("")
#
#         driver.find_element_by_link_text('免费注册').click()
#         driver.find_element_by_id('username').send_keys(i[0])     #循环输入dictvar中的username数据
#         driver.find_element_by_id('email').send_keys(i[1])           #循环输入dictvar中的email数据
#         driver.find_element_by_id('password').send_keys(i[2])     #循环输入dictvar中的password数据
#         driver.find_element_by_id('repassword').send_keys(i[3])  #循环输入dictvar中的repassword数据
#         driver.find_element_by_link_text('立即注册').click()
#         time.sleep(3)
#
#         expect = i[4]                           #循环输入dictvar中的expect数据
#         actvalue = driver.find_element_by_xpath('')     #定位到注册失败的提示信息
#
#         if expect==actvalue:
#             print("注册的反向测试用例通过")
#         else:
#             print('注册的反向测试用例不通过')
#         driver.quit()



"""
excel:
      1.安装xlrd模块，
      2.导包，
      3.使用xlrd模块打开execl文件 
      4.读取其中某一个sheet数据,索引从0开始
         第一种方法： tab = data.sheets()[0]
         第二种方法:  tab = data.sheet_by_name("sheet页的名字")
      5.获取某一行数据:row_value(0)    col_value(0)
      6.获取行数或者列数：nrows、ncols
      7.使用for循环获取每一个单元格数据
        for i in range(总行数):
            print(table.row_values(i)[0])
      
"""
# import xlrd
# data = xlrd.open_workbook(r"./execl_001.xlsx")   #使用xlrd提供的方法打开execl文件，并将文件的数据读取出来
# datatable = data.sheets()[0]          #获取索引为0的sheet页，也就是sheet1
# datatable.row_values(0)              #获取sheet页中指定的行数据
# datatable.col_values(0)              #获取sheet页中指定的列数据    datatable.cell(0,1).value  #拿到第一行第二列的数据
#
# #nrow = datatable.nrows          #获取总行数 4行
# #ncol = datatable.ncols          #获取总列数 5列
# #print(nrow)
#
# for i in range(nrow):
#     print(datatable.row_values(i)[0])       #拿到所有行数据，索引0代表拿到第一行数据
#     driver = webdriver.Chrome()
#     driver.get("")
#
#     driver.find_element_by_link_text('免费注册').click()
#     driver.find_element_by_id('username').send_keys(datatable.row_value(i)[0])     #循环输入dictvar中的username数据
#     driver.find_element_by_id('email').send_keys(datatable.row_value(i)[1])           #循环输入dictvar中的email数据
#     driver.find_element_by_id('password').send_keys(datatable.row_value(i)[2])     #循环输入dictvar中的password数据
#     driver.find_element_by_id('repassword').send_keys(datatable.row_value(i)[3])  #循环输入dictvar中的repassword数据
#     driver.find_element_by_link_text('立即注册').click()
#     time.sleep(3)
#
#     expect = datatable.row_value(i)[4]               #循环输入dictvar中的expect数据
#     actvalue = driver.find_element_by_xpath('')     #定位到注册失败的提示信息
#
#     if expect==actvalue:
#         print("注册的反向测试用例通过")
#     else:
#         print('注册的反向测试用例不通过')
#     driver.quit()








