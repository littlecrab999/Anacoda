# -*- coding: utf-8 -*-
"""
Created on Sun May 01 12:24:13 2016

@author: jennychan
"""

import os
import sys
import numpy as np
from sklearn.externals import joblib
from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def textClassify(data_dir):
    moviereviews=load_files(data_dir)
    train_data,test_data,train_class,test_class= \
    train_test_split(moviereviews.data,moviereviews.target,test_size=0.2)
    
    count_vec=CountVectorizer(binary=True)
    test_vector=count_vec.fit_transform(test_data)
    train_vector=count_vec.transform(train_data)
    
    clf=MultinomialNB().fit(train_vector,train_class)
    class_predict=clf.predict(test_vector)
    #save model
    joblib.dump(clf, "train_model.m")
    print 'Accuracy:' ,np.mean(class_predict==test_class)
    
if __name__ =='__main__':
    data_dir="txt_sentoken"
    textClassify(data_dir)