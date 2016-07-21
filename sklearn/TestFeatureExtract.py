# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:05:10 2016

@author: jennychan
"""

from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

from sklearn.feature_extraction.text import CountVectorizer
countv=CountVectorizer()
X_traincount=countv.fit_transform(twenty_train.data)
print twenty_train.target
from sklearn.feature_extraction.text import TfidfTransformer

tf=TfidfTransformer(use_idf=False).fit(X_traincount)