# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:44:08 2016

@author: jennychan
"""
import numpy as np
from numpy import *
def loadData(file):
    f=open(file)
    dataset=[]
    label=[]
    for line in f.readlines():
        d=line.split()
        dataset.append(d[1:6])
        label.append(d[0])
    return dataset,label
    
dataset,label=loadData('testdata.txt')


def countProb(label):
    #dataset=mat(dataset)
    prob={'0':0,'1':0}
    m=len(label)
    c0=label.count('0')
    c1=label.count('1')
    prob['0']=float(float(c0)/m)
    prob['1']=float(float(c1)/m)
    return prob
'''
A:data column
label:datalabel
probl:label probility
'''  
def  countConProb(A,label,probl):
    #label=0
    #countC0={'0':0,'1':1}
    #label=1
    #countC1={'0':0,'1':1}
    
    m=len(label)
    conn=[]
    prob={'00':0,'01':0,'10':0,'11':0}
    for i in range(m):
        c=A[i,0]+label[i]
        conn.append(c)
    c0=conn.count('00')
    c1=conn.count('10')
        #joint probility
    prob['00']=float(float(c0)/m)
        #conditional probility
    prob['00']=prob['00']/probl['0']
    prob['10']=float(float(c1)/m)
    prob['10']=prob['10']/probl['0']
   
    c0=conn.count('01')
    c1=conn.count('11')
    prob['01']=float(float(c0)/m)
    prob['01']=prob['01']/probl['1']
    prob['11']=float(float(c1)/m)
    prob['11']=prob['11']/probl['1']
        
    return prob
        
def main():
    dataset,label=loadData('trainingdata.txt')
    dataset=mat(dataset)
    m,n=shape(dataset)
    probl=countProb(label)
    print 'prob of label: %s' %probl 
    condProb=[]
    for i in range(n):
        A=dataset[:,i]
        prob=countConProb(A,label,probl)
        if i==1:
            print 'conditional prob of A1:%s' %(prob)
        condProb.append(prob)
    testdata,testlabel=loadData('testdata.txt')
    newlabel=[]
   # print condProb
    m=len(testdata)
    for i in range(m):
        A=testdata[i]
        prob0=1.0;prob1=1.0
        for j in range(len(A)):
            #calc prob0,prob1
            if(A[j]=='0'):
                prob0=prob0*condProb[j]['00']
                prob1=prob1*condProb[j]['01']
            else:
                prob0=prob0*condProb[j]['10']
                prob1=prob1*condProb[j]['11']
        prob0=prob0*probl['0']
        prob1=prob1*probl['1']
        if(prob0>prob1):
            newlabel.append('0')
        else:
            newlabel.append('1')
    

    count=0
    for i in range(m):
        if(newlabel[i]==testlabel[i]):
           count+=1
    print (1.0-float(float(count)/m))
          
    #print newlabel
            
main()
    

    
        

        
                
    
    

    

    
    
        
        