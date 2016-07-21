# -*- coding: utf-8 -*-
"""
Created on Tue May 03 14:39:00 2016

@author: jennychan
"""
import numpy as np
import matplotlib.pyplot as plt
def loadData(file):
    f=open(file)
    datamat=[]
    for line in f.readlines():
        data=line.split();
        dataf=[]
        for n in data:
            n=float(n)
            dataf.append(n)
        datamat.append(dataf)
    return datamat
    
datamat=loadData('testdata1.txt')
print np.shape(datamat)

def pca(data,length):
    data=np.mat(data)
    meanval=np.mean(data,axis=0)
    rmmval=data-meanval
    covmat=np.cov(rmmval,rowvar=0)
    eival,eivec=np.linalg.eig(np.mat(covmat))
   # print eivec
    tfmat=eivec[:,0:length]
   # print tfmat
    finaldata=data*tfmat
    return finaldata
    
finaldata=pca(datamat,3)
print finaldata
print finaldata[18,:]
plt.figure(1)
#plt.plot(finaldata[:,0],finaldata[:,1])