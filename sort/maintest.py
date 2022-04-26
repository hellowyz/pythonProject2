"""
这是一个主测试文件，不是用来写测试用例的，而是用来组织测试用例执行的

"""
import unittest
from HtmlTestRunner import HTMLTestRunner
import os
import time
# 第一种
#  导包的方式太麻烦，而且用例要一个一个导包，该方法pass
# from unittest_copy import mymath
# suitt = unittest.TestSuite
# suitt.addTest(mymath("test_jia_1"))

# 第二种
# 该方法测试运行结果在txt文本中，看起来费劲不美观
# discover = unittest.defaultTestLoader.discover(r"./",pattern=("unittest_copy"))

# with open(r"./re.txt", "w", encoding="utf-8") as f:
#     runner = unittest.TextTestRunner(f, descriptions="测试用例执行", verbosity=2)
#     runner.run(discover)

# 第三种
# runner运行器是unittest自带的，效果不是很好，我们第三方开发的来用，可以用HTML展示效果
# HTMLTestRunner模块，是一个第三方模块,在pycharm终端下载 pip install html-TestRunner,然后导包from import

discover = unittest.defaultTestLoader.discover(r"../selenium/", pattern=("unittest_copy"))

# 能不能把每次执行过的报告都保留，用执行时间当做HTML文件名
filename = time.strftime("%Y-%m-%d-%H-%M-%S")+r".html"
path = os.path.dirname(__file__)+r"/"
filename = path+filename

# w:字符形式写入,文本文件可以，视频图片直接用w写不进去，只能以b形式写入 "rb" "wb"
with open(filename,"wb") as f:
    runner = HTMLTestRunner(f,verbosity=2,report_title='单元测试报告',descriptions="第一次运行结果")
    runner.run(discover)



