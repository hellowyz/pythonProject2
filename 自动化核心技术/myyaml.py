""""
语法：
1.大小写敏感
2.使用缩进标识层级关系
3.缩进不允许使用tab键，只允许空格
4.缩进的空格数不重要，只要相同层级的元素对其即可
5.#标识注释

yaml对象：
写法1：对象键值对使用冒号结构标识key: value (冒号后面要加一个空格)
写法2：key:
        key1: value1
        key2: value2
        key3: value3
写法3：数组，(列表list)，用一组横行“-”开头，
    如：msxy:
          - name: 百里
          - age: 18

纯量的基本使用：
defaults: &defaults
   adapter: postgres
   host:    localhost

development:
   database: myapp_development
   <<: *defaults
相当于：
defaults:
   adapter: postgres
   host:    localhost

development:
   database: myapp_development
   adapter: postgres
   host:    localhost
&用来建立锚点（defaults），<<表示合并到当前数据，*用来引用锚点
"""
# python通过open方式读取文件数据，再通过load函数将数据转化为列表或字典
import yaml
import os
path = os.path.dirname(os.path.dirname(__file__))+r"/requests/request.yaml"
with open(path,"r",encoding="utf-8")as f:
    data = f.read()
    # f.close()

    a = yaml.load(data,Loader=yaml.FullLoader)     # FullLoader 表示全局加载
    print(a)

# 读取yaml文件
def read_yaml(self,key):
    with open(os.getcwd()+"",mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

# 写入yaml文件
def write_yaml(self,data):
    with open(os.getcwd()+"",mode='a',encoding='utf-8') as f:
        yaml.dump(data=data,stream=f,allow_unicode=True)

# 清除yaml文件
def clear_yaml(self):
    with open(os.getcwd()+"",mode='w',encoding='utf-8') as f:
        f.truncate()