
'''
日志等级：
DEBUG:  最详细的日志信息，典型应用场景就是 问题诊断
INFO:  信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期那样进行工作
WARNING: 当某些不同期望的事情发生时记录的信息(如:磁盘可用空间较低)，但是此时应用还是正常运行的
ERROR:由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL:发生严重错误，导致应用程序不能继续运行时记录的信息
'''

# fot = "%(name)s--->%(message)s--->%(asctime)s"
# logging.basicConfig(filename='my.log',level="DEBUG",format=fot)   # 生成文件，设置日志级别和时间格式和日志信息
#
# logging.debug("这是debug信息")
# logging.info("这是info信息")
# logging.warning("这是warning信息")
# logging.error("这是error信息")
# logging.critical("这是cri信息")

'''
Logging.Logger：Logger是Logging模块的主体，进行以下三项工作：
1. 为程序提供记录日志的接口
2. 判断日志所处级别，并判断是否要过滤
3. 根据其日志级别将该条日志分发给不同handler
常用函数有：
Logger.setLevel() 设置日志级别
Logger.addHandler() 和 Logger.removeHandler() 添加和删除一个Handler
Logger.addFilter() 添加一个Filter,过滤作用

format常用格式说明
%（acstime)s 时间
%（filename)s 日志文件名
%（funcName)s 调用日志的函数名
%（levelname)s 日志的级别
%（module)s 调用日志的模块名
%（message)s 日志信息
%（name)s logger的name，不写的话默认是root

'''
# 1.创建日志对象logger
# logger = logging.getLogger()
#
# # 2.创建控制台处理器
# console_handler = logging.StreamHandler()
# logger.setLevel("DEBUG")        # log等级为debug
# # 3.控制台等级
# console_handler.setLevel(level="WARNING")
#
# # 日志器添加控制台处理器
# logger.addHandler(console_handler)
#
# logging.debug("这是debug信息")
# logging.info("这是info信息")
# logging.warning("这是warning信息")
# logging.error("这是error信息")
# logging.critical("这是cri信息")

# log = logging.getLogger()        # 创建日志器对象
# log.setLevel(logging.DEBUG)      # 设置日志等级
#
# hander1 = logging.StreamHandler()   # 创建控制台对象，将日志消息发送到输出到Stream
# hander2 = logging.FileHandler('hello.log',mode="w",encoding="utf-8")   # 将日志消息发送到磁盘文件
#
# hander1.setLevel(logging.INFO)   # 设置handler将会处理的日志消息的最低严重级别
# hander2.setLevel(logging.DEBUG)
#
# matter1 = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
# matter2 = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
#
# hander1.setFormatter(matter1)     # 为handler设置一个格式器对象
# hander2.setFormatter(matter2)
#
# log.addHandler(hander1)    # 日志器添加控制台处理器
# log.addHandler(hander2)    # 日志器添加控制台处理器
#
# log.info("我是info信息")
# log.debug("我是debug信息")
# log.warning('我是warning信息')
# log.error('我是error信息')
# log.critical('我是critical信息')


''''
现在有以下几个日志记录的需求：
1）要求将所有级别的所有日志都写入磁盘文件中
2）all.log文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
3）error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
4）要求all.log在每天凌晨进行日志切割

'''

import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# MIDNIGHT 指的是，只要过了0点就会滚动。
# interval 是间隔时间单位的个数，指等待多少个 when 的时间后 Logger 会自动重建新闻继续进行日志记录
# backupCount 是保留日志的文件个数
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')