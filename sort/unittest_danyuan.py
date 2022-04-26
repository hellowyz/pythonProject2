"""
之前脚本存在的问题
1.在测试用例执行时候，发现挺麻烦（如果测试用例数量过多）
2.断言方式太low，只能是通过在控制台打印测试用例是否通过，我们希望这个断言的状态是显示在报告
而不应该通过if else去判断
3.基本看不到测试报告的效果，显示总共执行了多少条用例，通过了多少条，失败了多少条，失败原因是什么

单元测试：
包括两部分：代码级别的功能验证，逻辑覆盖
单元测试框架的好处：
1.提供用例组织和执行
2.提供丰富的断言方法
3.提供丰富的日志和报告（HTML格式）

"""

"""
使用unittest框架来设计单元测试用例（通过这个案例讲解unittest的特性）
步骤：
1.导包，unittest是自带的框架，不需要安装
2.创建一个单元测试类（其实就是类，只不过继承了单元测试框架单元测试用例的类）
3.单元测试类中的五个特殊的方法使用，包括使用场景及执行顺序
   setUp()、test_xxx()、tearDown(),不管怎么调整，执行顺序不变
   setUp():主要是进行测试用例的资源初始化
   test_xxx():测试用例，把测试用例的步骤写在这个方法中
   tearDown():主要进行测试用例的资源释放
   @classmethod:注解的方法是类方法，不用创建对象也能用的方法，在对象进内存前就存在的方法
                 随着类一起进的内存
     setUpClass:给当前单元测试类的所有用例进行初始化
     tearDownClass:给当前单元测试类的所有的用例进行资源释放
4.创建测试用例：test开头的方法
5.测试用例执行：main()：把所有的测试用例执行一遍，执行用例的顺序控制不了（按照测试用例名的字母顺序执行的）
             如何解决这个不太好的特点，使用测试集合概念testsuite分类，我要把加法的测试用例加到一个测试集合testsuite中
             只运行该测试集合即可
             testsuite：1.创建testsuite的对象 
                        2.调用testsuite中的方法addtest、addtests()将测试用例加入测试集合
                        3.testsuite的run()方法运行测试集合,注意:run方法的参数是testresult的对象：re = unittest.testResult()
                           testresult存储的是测试执行的结果
                           print(re.__dict__)可以把执行的结果以字典形式展示出来
             TestLoader:1.创建TestLoader对象：loader = unittest.TestLoader()
                        2.使用loader的方法loadtestsfromName()将指定的测试用例加载到测试集合，并返回到
                           loadtestsfromName()的参数比较灵活
                           1.可以是模块名，2.可以是模块中的类名，3.可以是模块中的类的某一用例：  
                        3.使用loader的discover方法（必须掌握），将指定文件（模块）中的测试用例一次性加载
                        discover()方法：suitt = unittest.defaultTestLoader.discover(r"./",pattern="")
                        path:指定存放测试用例的目录即可(单元测试用例，使用unittest框架写的测试用例)
                        pattern：指定匹配规则，very_reg_*.py
                                            very_login_*.py
             TestRunner:在前面测试用例、测试集合执行的时候都是用testsuite()的run方法：su.run(result)            
                        TextTestRunner():将结果能够以text文本形式展示的运行器
                        使用TextTestTRunner()运行器提供的run()方法运行测试集合
                        如何产生一个文件流对象，如果打开一个文本文件，往里写数据
                        报告是以TextTestResult的形式展示的
                        TextTestRunner是TestRunner的子类  

                        with open(r"./re.txt","w",encoding="utf-8") as f:
                            runner = unittest.TextTestRunner(f,descriptions="单元测试报告",verbosity=2)
                            runner.run(su)
断言：一个自动化测试用例，测试步骤、断言缺一不可
unittest提供的断言方法有：assertEqual(a,b,msg=""):就是判断a和b是否相等，则断言成功，如果不相等则断言失败，并且输出msg消息



                                  
Unittest单元测试框架的工作原理:
>TestCase:一个TestCase的实例就是一个测试用例。什么是测试用例呢?就是一个完整的测试流程，
包括测试前准备环境的搭建(setUp)，
执行测试代码(test)，
以及测试后环境的还原(tearDown),
>TestSuite:多个测试用例集合在一起，就是TestSuite。
>TestLoader是用来加载TestCase到TestSulte中，只中有UTua 5o人ToctSrite就例、各个地方寻找TestCase,创建它们的实例，
然后add到TestSuite中,再返回一个TestSuite实例。

"""

import unittest
from data.my import mymath

class unitMy(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("我是setUpClass方法")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("我是tearDownClass方法")

    def setUp(self):             #测试用例资源初始化，setUp是方法名，不能改
        self.mm = mymath
        # print("我是setUp方法")

    def test_add_1(self):        #必须是test开头的方法，这就是一个测试用例
        print("我是第1条测试用例")
        actValue = self.mm.jia(5,5)        #实际结果
        expValue = 10                      #预期结果
        self.assertEqual(actValue,expValue,"预期和实际结果不符")

    def test_jian_1(self):
        actValue = self.mm.jian(5,3)
        expValue = 2
        self.assertEqual(actValue, expValue, "预期和实际结果不符")
        # print("我是第2条测试用例")

    def test_cheng_1(self):
        actValue = self.mm.cheng(2,7)
        expValue = 4
        self.assertEqual(actValue, expValue, "预期和实际结果不符")
        # print("我是第3条测试用例")

    def test_cheng_2(self):
        actValue = self.mm.cheng('a',2)
        expValue = 'aa'
        self.assertEqual(actValue, expValue, "预期和实际结果不符")
        # print("我是第4条测试用例")

    def tearDown(self):             #方法名不能更改
        #注销对象，释放资源
        pass
        # print("我是tearDown方法")

if __name__ == '__main__':
    unittest.main()                 #调用执行单元测试类，通过主方法main执行，该方法是执行全部测试类中的全部测试用例

    # su = unittest.TestSuite()
    # su.addTest(unitMy("test_cheng_2"))       #addTest追加单个测试用例到测试集合
    # su.addTests(map(unitMy,["test_add_1","test_cheng_2"]))    #addTests追加多个测试用例到测试集合

    #如果测试用例数量比较大，使用testsuite自带的方法加用例到集合，很麻烦
    # 可以unittest中提供的testloader模块，提供了好多帮我们把测试用例加载到测试集合中的方法
    # 创建testloader对象
    # loader = unittest.TestLoader()
    # loadTestsFromName:通过添加一个模块xx名、类名、测试用例名，将其中的用例直接加载到测试集合
    # stu = loader.loadTestsFromName("unittest_danyuan.unitMy.test_add_1")

    # 使用TestLoader对象的discover方法加载用例,是将指定路径所有符合匹配规则（pattern）文件中的单元测试用例一次性加载
    # 第一个参数是一个目录，这个目录下可以有单元测试用例的文件(.py)
    # "unit*.py"指的是以unit开头，以.py结尾的文件，pattern中一定是unit开头的模块test开头的测试用例才能被加载进来
    # discover = unittest.defaultTestLoader.discover(r"./",pattern="unit*.py")

    # 测试结果
    # re = unittest.TestResult()
    # su.run(re)                         #测试集合中有run方法，直接运行

    #使用TextTestTRunner()运行器提供的run()方法运行测试集合
    #如何产生一个文件流对象，如果打开一个文本文件，往里写数据
    #报告是以TextTestResult的形式展示的
    #TextTestRunner是TestRunner的子类

    # with open(r"./re.txt","w",encoding="utf-8") as f:
    #     runner = unittest.TextTestRunner(f,descriptions="单元测试报告",verbosity=2)
    #     runner.run(su)












