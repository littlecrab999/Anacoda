# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:10:54 2016

@author: jennychan
"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris=load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species']=pd.Series(iris.target)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df.head()

train, test = df[df['is_train']==True], df[df['is_train']==False]

label=df.columns[4]
features = df.columns[:4]
y=train[label]
clf = RandomForestClassifier(n_jobs=2)
clf.fit(train[features],train[label])

pred=clf.predict(test[features])
print pred
print list(test[label])
print pred==list(test[label])
#print sum(sum([pred==list(test[label])]))/float(len(pred))



#preds = iris.target[clf.predict(test[features])]
#print preds
print pd.crosstab(test['species'], pred, rownames=['actual'], colnames=['preds'])