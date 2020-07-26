#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_study -> test_2
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/5/10 10:22
@Desc   ：
=================================================='''




import holoviews as hv
import pandas as pd
hv.extension('bokeh')
hv.output(fig='html', size=300)

data = pd.read_csv('seven.csv',index_col=0,header=0)
germany_data = data.loc['德国'].values
france_data = data.loc['法国'].values
britain_data =[1000,2000,3000,4000,5000]

dims =dict(kdims='时间/天', vdims='新增肺炎人数')
l1 = hv.Area(germany_data, label='法国', **dims)
l2 = hv.Area(britain_data, label='英国', **dims)
l3 = hv.Area(france_data, label='德国', **dims)
overlay = (l1*l2*l3)
hv.save(overlay, 'a.html', fmt='html')