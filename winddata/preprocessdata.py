# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:43:33 2016

@author: jennychan
"""

import os
def loadData():
    MINSIZE=1400
    fr=open(r"./data/HTL_LL_019_20160506144822.txt")
    fw=open(r"./data/processeddata1.txt",'w+')
    line=fr.readline()
    lineArr=line.strip().replace("{","").replace("\"","").replace(":",",").split(',')
    #print len(lineArr)
    column=[]
    for i in range(len(lineArr)):
        if i%2==1:
            column.append(lineArr[i])
    column=column[3:]
    for s in column:
        fw.write(s)
        fw.write("\t")
    fw.write("\n")
    datafiles=os.listdir(r"./data")
    for datafile in datafiles:
        fr=open(r"./data/"+datafile)
        count=0
        lines=fr.readlines()
        for line in lines:
            if count<MINSIZE:
                count+=1
                continue
            else:
                lineArr=line.strip().replace("{","").replace("\"","").replace(":",",").split(',')
                for i in range(len(lineArr)):
                    if i>6 and i%2==0:
                        fw.write(lineArr[i]+"\t")
                fw.write("\n")
                        
                
            
loadData()
print "\t"
            