# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 09:54:27 2020

@author: Yue
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:23:55 2020

@author: Yue
"""
# 导入输出图片工具
from pyecharts.charts import Bar
from pyecharts import options as opts

def hardcode_html_python():
    # V1 版本开始支持链式调用
    bar = (
        Bar()
        .add_xaxis(["奶茶", "咖啡", "蛋糕", "牛奶", "可乐", "王老吉", "北冰洋"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
    )
    bar.render()
    return