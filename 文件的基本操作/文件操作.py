#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> 文件操作
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/5/4 22:01
@Desc   ：
=================================================='''

# 1、打开文件
# f = open("文件路径")
#
# # 2、操作文件：读写文件
# res=f.read()
#
# # 3、关闭文件
# f.close() # 回收操作系统资源
# # del f 回收应用程序资源


with open("11",mode="rt",encoding="utf-8") as f1:
    a = f1.read()
print(a)