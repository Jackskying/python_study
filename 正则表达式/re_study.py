#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re

# 查找
# findall 返回列表 匹配所有，每一项都是列表中的一个元素
ret = re.findall("\d+","dsdw343的观点") # 三个参数表示正则表达式，待匹配的字符串，flag
print(ret)
# search:返回一个变量 只匹配从左到右的第一个，得到的不是直接的结果，而是一个变量 这个变量通过group方法获取结果
# 如果没有匹配到，会返回None，用group会报错
ret1 = re.search("\d+","dsdw343的观点") # 三个参数表示正则表达式，待匹配的字符串，flag
print(ret1) # 内存地址
print(ret1.group()) # 通过ret.group()获取真正的结果
# match  从头开始匹配

# 字符串处理的扩展：替换 切割
# split 返回列表 根据正则表达式切割
s = "alexdsada343dasfe546e"
ret2 = re.split("\d+",s)
print(ret2)
# sub  谁 旧的 替换成新的 次数
re.sub("\d+","e",s)

# subn 会返回一个元组 第二个元素是替换的次数

# re模块的进阶
# compile 节省解决问题的时间
# 编译 正则表达式 编译成字节码
# 在多次使用过程中 不会多次编译
ret = re.compile("\d+")
print(ret)
s = "alexdsada343dasfe546e"
res = ret.findall(s)
print(res)

# finditer 节省解决问题的空间
ret = re.finditer("\d+","ddsd3499ji39")
print(ret)
for i in ret:
    print(i.group())