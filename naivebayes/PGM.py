# -*- coding: utf-8 -*-
"""
Created on Mon May 02 18:31:02 2016

@author: jennychan
"""

import networkx as nx
import numpy 
import math
from numpy import*
def loadData(file):
    f=open(file)
    dataset=[]
    label=[]
    for line in f.readlines():
        d=line.split()
        dataset.append(d[1:6])
        label.append(d[0])
    return dataset,label
    
dataset,label=loadData('trainingdata.txt')
dataset=mat(dataset)
A=dataset[:,0]

print sum(A=='0')

def calcMultinfo(dataset):
    m,n=shape(dataset)
    multinfos={}
    for i in range(n):
        onecol=dataset[:,i]
        prob1={}
        prob1['0']=sum(onecol=='0')/float(m)
        prob1['1']=sum(onecol=='1')/float(m)
        for j in range(i+1,n):
            anocol=dataset[:,j]
            prob2={}
            prob2['0']=sum(anocol=='0')/float(m)
            prob2['1']=sum(anocol=='1')/float(m)
            joincols=[]
            for k in range(m):
                joincol=onecol[k,0]+anocol[k,0]
                joincols.append(joincol)
            joinprob={}
            joinprob['00']=joincols.count('00')/float(m)
            joinprob['01']=joincols.count('01')/float(m)
            joinprob['10']=joincols.count('10')/float(m)
            joinprob['11']=joincols.count('11')/float(m)
            
            multinfo=0.0
            for k,v in joinprob.iteritems():
                index1=k[0]
                index2=k[1]
                sepprob=prob1[index1]*prob2[index2]
                multinfo+=v*math.log(v/sepprob)
            k1=str(i+1)
            k2=str(j+1)
            key=k1+k2
            multinfos[key]=multinfo
    multinfos=sorted(multinfos.items(),key=lambda d:d[1],reverse=True)
    return multinfos
    
multinfos=calcMultinfo(dataset)
#print multinfos
def MWST(multinfos,n):
    usednodes=[]
    stree={}
    count=0
    for item in multinfos:
        if count==n: break
        k=item[0]
        v=item[1]
        if usednodes.count(k[0])==1 and usednodes.count(k[1])==1:
            continue
        stree[k]=v
        usednodes.append(k[0])
        usednodes.append(k[1])
        count+=1
    return stree
    
stree=MWST(multinfos,4)
print stree

def plotTree(stree):
    graph=nx.Graph()
    for k,v in stree.iteritems():
        node1=k[0]
        node2=k[1]
        graph.add_node(node1,name='A'+node1)
        graph.add_node(node2,name='A'+node2)
        graph.add_edge(node1,node2,weight=v)
    return graph

graph=plotTree(stree)
nx.draw_networkx(graph)
            
        
