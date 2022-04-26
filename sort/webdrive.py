# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com")

# title=driver.title        #获取页面的title

# driver.find_element_by_id("kw").send_keys("selensium")

# time.sleep(2)
# driver.find_element_by_id("kw").clear()      #清除文本
# driver.find_element_by_id('kw').send_keys('城哥')
# time.sleep(2)
# driver.find_element_by_id("su").click()     #单击元素，例如按钮，超链接，单选框，复选框操作
# #
# time.sleep(2)
# driver.quit()


# driver.find_elements_by_link_text('新闻').click()
# url=driver.current_url                #获取新闻页面的url
# print(url)
# #加断言
# driver.quit()

#text,get_attribute(),is_displayde()用处
# wenben=driver.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]').text
# print(wenben)  #text获取文本
#
# value1=driver.find_element_by_id('kw').get_attribute('name') #get_attribute获取文本框的属性值，如文本框name属性值为wd
# print(value1)                                                #如果是get_attribute(value)可以获取文本框内的值
# driver.quit()
#
# if driver.find_element_by_id('su').is_displayed():     #设置该元素是否可见，结果为真或假
#     print('百度一下按钮显示了')
# else:
#     print('显示失败')


# ############页面窗口大小
# driver.set_window_size(1920,600)     #打开页面窗口尺寸
# driver.maximize_window()            #最大化显示窗口
# driver.minimize_window()            #最小化


##############页面的前进后退操作
# driver.find_element_by_link_text('新闻').click()
# time.sleep(2)
# driver.back()             #回退到上一操作
# time.sleep(2)
# driver.forward()          #前进到新闻页面
# time.sleep(2)
# driver.refresh()          #刷新页面操作


# ##############保存截屏文件
# driver.save_screenshot(r'e:\ss.png')
# time.sleep(2)
# driver.quit()     #关闭所有页面
# driver.close()    #关闭单个窗口


################页面句柄
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('https://www.taobao.com')
# time.sleep(2)
#
# han1=driver.current_window_handle       #获取当前页面的句柄
# print(han1)
#
# driver.find_element_by_link_text('聚划算').click()
# time.sleep(2)
#
# han2=driver.window_handles   #获取所有页面的句柄值
# print(han2)
# driver.switch_to.window(han2[1])            #取拿到所有句柄值的第二个，把聚划算的句柄绑定给drive
#
# driver.find_element_by_link_text('请登录').click()
# time.sleep(2)
# driver.back()                               #回退
# driver.close()                              #关闭当前窗口


##################鼠标，键盘操作
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# time.sleep(2)

#################控制鼠标悬浮到设置按钮上
# set=driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(set).perform()     #将对设置按钮的操作行为封装到ActionChains
# time.sleep(3)                                           # perform() 执行所有ActionChains中储存的行为

##################鼠标右键
# edi=driver.find_element_by_id('kw')
# ActionChains(driver).context_click(edi).perform()  #在百度文本框点击右键
# time.sleep(3)
# driver.quit()

#################键盘事件
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys             #导入键盘事件包
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.find_element_by_id('kw').send_keys('周哥啊')
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)   #删除多输入的‘啊’
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(' 太帅了')          #再次输入太帅了，和前面的字符串拼接
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')  #全选文本框内容
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')  #剪切文本框内容
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')  #粘贴文本框内容
# time.sleep(1)
# driver.find_element_by_id('kw').send_keys(Keys.ENTER)        #回车键代替单击，完成搜索
# time.sleep(1)
# driver.quit()


###################警告窗操作
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# time.sleep(2)
# driver.maximize_window()                     #最大化窗口
# time.sleep(2)
# a = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')     #用xpath定位设置按钮
# ActionChains(driver).move_to_element(a).perform()                   #对设置按钮进行悬停操作
# time.sleep(2)
# driver.find_element_by_link_text('搜索设置').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="s1_2"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="nr_2"]').click()
# time.sleep(2)
# driver.find_element_by_link_text('保存设置').click()       #点击保存设置，弹出警告框
# time.sleep(2)
# a = driver.switch_to.alert.text                          #获取警告框文本信息
# print(a)
# time.sleep(2)
# driver.switch_to.alert.accept()                          #接受现有警告框
# time.sleep(2)
# # driver.switch_to.alert.dismiss()                       #放弃现有警告框
# # time.sleep(2)
# driver.quit()


################### 多表单操作
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.qq.com')                 #输入qq地址
time.sleep(2)
driver.find_element_by_xpath('//*[@id="top-login"]/div[2]/a').click()    #定位到登入按钮，点击
time.sleep(2)
han = driver.window_handles                      # 获取所有页面句柄
driver.switch_to.window(han[1])                  # 绑定到第二个句柄
driver.switch_to.frame('login_frame')            # 绑定frame表单，frame表单名找他的上级iframe
time.sleep(2)
driver.find_element_by_xpath('//*[@id="u"]').send_keys('2478206298')      # 输入用户名
time.sleep(2)
driver.find_element_by_xpath('//*[@id="p"]').send_keys('12345456')        # 输入密码
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_button"]').click()          # 点击登录
time.sleep(2)
driver.quit()

# #################元素等待
# 强制等待：time.sleep()
# 隐形等待：driver.implicity_wait(10)
#         在脚本创建driver对象后，给driver设置一个全局的等待时间，对driver的整个生命周期都起效
#         如果在设置等待时间内，定位到页面元素，则不再等待，继续执行下面代码，超出时间抛出异常

