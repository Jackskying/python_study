#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> 账号密码
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/5/23 22:31
@Desc   ：
=================================================='''


name = input("请输入名字：")
passwd = input("请输入密码：")
with open("did.txt",mode="at",encoding="utf-8") as f:
    f.write("{}:{}\n".format(name,passwd))

# 文件的拷贝功能

# src_file = input("请输入源文件的路径：").strip()
# dst_file = input("请输入目的文件的路径：").strip()
# with open(r"{}".format(src_file),mode="rt",encoding="utf-8") as f1,\
#     open(r"{}".format(dst_file),mode="wt",encoding="utf-8") as f2:
#     res = f1.read()
#     f2.write(res)


