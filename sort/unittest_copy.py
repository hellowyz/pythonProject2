import unittest
from data.my import mymath
class unitmy(unittest.TestCase):
    def setUp(self):
        self.mm = mymath

# 在测试用例中添加文档字符串，这样生成的报告就有相应的用例说明啦
    def test_jia_1(self):
        '''验证数字类型的加法运输'''
        actvalue = self.mm.jia(2,3)
        expvalue = 5
        self.assertEqual(actvalue,expvalue,"实际结果和预期不符")

    def test_jia_2(self):
        '''验证字符串类型的拼接运算'''
        actvalue = self.mm.jia('abc','def')
        expvalue = 'abcdef'
        self.assertEqual(actvalue,expvalue,"实际结果与预期结果不符")

    def test_jia_3(self):
        '''验证字整型数字和符串类型的拼接运算'''
        actvalue = self.mm.jia('abc','2')
        expvalue = 'abc2'
        self.assertEqual(actvalue, expvalue, "实际结果与预期结果不符")

    def tearDown(self):
        pass
if __name__ == '__main__':
    # unittest.main()
    #直接使用discover，使用runner运行器进行测试集
    discover = unittest.defaultTestLoader.discover(r"../selenium/", pattern="unittest_copy.py")
    with open(r"./re.txt","w",encoding="utf-8") as f:
        runner = unittest.TextTestRunner(f,descriptions="测试用例执行",verbosity=2)
        runner.run(discover)
        #结尾增加了一个注释