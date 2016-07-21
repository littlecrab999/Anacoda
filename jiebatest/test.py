# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:43:35 2016

@author: jennychan
"""

import jieba
'''
seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
print "Full Mode:", "/ ".join(seg_list) #全模式

seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
print "Default Mode:", "/ ".join(seg_list) #精确模式
'''
#jieba.enable_traditional_chinese()
seg_list = jieba.cut("你真是萌萌哒") #默认是精确模式
print ", ".join(seg_list)

