#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> b模式
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/5/25 23:25
@Desc   ：
=================================================='''

"""
t:
  1、读写都是以字符串为单位
  2、只能针对文本文件
  3、必须指定字符编码
b:
"""

# with open(r"",mode="") as f:
#     pass


# 循环读取文件
# 方式一：
with open(r"") as f:
    while True:
        res = f.read(1024)
        if len(res) == 0:
            break


#方式二：
with open(r"") as f:
    for line in f:
        print(line)
