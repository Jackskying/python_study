#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> list_study
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/5/3 17:31
@Desc   ：
=================================================='''

# 作用：按位置存放多个值
# 类型转换：但凡能够被for循环遍历的类型都可以当作参数给list()转成列表
# 内置方法
# 1、按索引取值 索引不存在则报错
# 2、切片（顾头不顾尾、步长）
# 3、长度
# 4、成员运算 in 和not in

# 5、追加
l = [1,"df","du"]
l.append("ko")
# 插入值 按照索引插入值
l.insert(1,"pl")
print(l)
# 合并列表 expend
b =[1,2,3]
l.extend(b)
print(l)
# 6、删除
# 方式1 del 公用的删除方法 没有返回值 不能进行赋值操作
del l[1]
# 方式二：pop根据索引删除 不指定索引默认删除最后一个
l.pop(1)
# 7、循环