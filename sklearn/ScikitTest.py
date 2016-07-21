# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:08:49 2016

@author: jennychan
"""

import numpy as np
import urllib
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

data=urllib.urlopen(url)
rawdata=np.loadtxt(data,delimiter=",")
X=rawdata[:,0:7]
y=rawdata[:,8]

from sklearn import preprocessing

normalized_x=preprocessing.normalize(X);

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(X, y)
# display the relative importance of each attribute
#print(model.feature_importances_)

from sklearn.linear_model import LogisticRegression
expected=y
model=LogisticRegression()
model.fit(X,y)
predict=model.predict(X)
print metrics.classification_report(expected,predict)
