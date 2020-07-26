#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> 检测文件处理
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/6/3 22:31
@Desc   ：
=================================================='''
import time

with open("did.txt",mode="rt",encoding="utf-8") as f:
    # 将文件指针移到末尾
    #
    f.seek(0,2)
    while True:
        line = f.readline()
        if len(line) == 0:
            time.sleep(0.3)
        else:
            print(line)

