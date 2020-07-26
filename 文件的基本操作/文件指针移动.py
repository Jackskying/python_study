#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> 文件指针移动
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/6/3 22:15
@Desc   ：
=================================================='''
# 0:参照物是文件开头位置
# 1：参照物是当前指针所在位置
#2：参照物是文件末尾位置，应该倒着移动

with open("did.txt",mode="rt",encoding="utf-8") as f:
    a = f.seek(1,0)
    print(a)
    f.seek(3,0) # 控制指针移动方式
    f.tell()# 获取指针位置


    