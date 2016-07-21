# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:27:25 2016

@author: jennychan
"""
import numpy as np
from sklearn import datasets,svm

svc=svm.SVC(C=1,kernel='linear')
iris=datasets.load_digits();
x_fold=np.array_split(iris.data,3)
y_fold=np.array_split(iris.target,3)
#print x_fold
score=list()
for i in range(3):
    x_train=list(x_fold)
    x_test=x_train.pop(i)
    x_train=np.concatenate(x_train)
    y_train=list(y_fold)
    y_test=y_train.pop(i)
    y_train=np.concatenate(y_train)
    score.append(svc.fit(x_train,y_train).score(x_test,y_test))
    
print score
    
    

