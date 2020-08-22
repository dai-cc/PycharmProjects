# -*- coding: utf-8 -*-
import unittest, csv
import os, sys
import time
import HTMLTestRunner


# 手工添加案例到套件，
def createsuite():
    discover = unittest.defaultTestLoader.discover('../HTMLreport', pattern='test*.py', top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # 1. 创建存放HTML报告的文件夹
    curpath = sys.path[0]
    print(sys.path)
    print("====================")
    print(sys.path[0])
    # 如果当前文件夹下resultreport文件夹不存在，生成文件夹resultreport
    # 获取当前文件夹路径可以用上述方法，也可以直接用 ./ 
    if not os.path.exists(curpath + '/resultreport'):
        os.makedirs(curpath + '/resultreport')

    # 2. 创建输出HTML报告
    # 取当前时间
    # time.time() 获取1970年到当前时间的格林威治时间戳
    # time.local(时间戳) 将时间戳本地化
    # time.strftime("想输出的时间格式"，时间) 对事件格式化
    # 引入时间戳是为了不让生成的HTML报告名字重复
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    # 得到HTML报告的名称
    filename = curpath + '/resultreport/' + now + 'resultreport.html'

    # 3. 跑测试套件生成HTML测试报告
    # 以wb（写）的方式打开HTML文件
    with open(filename, 'wb') as fp:
        # 出html报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况',verbosity=2)
        suite = createsuite()
        runner.run(suite)