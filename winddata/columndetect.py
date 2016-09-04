# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:52:50 2016

@author: jennychan
"""
import os
import numpy as np

def loadColumn():
    fr=open(r"./data/HTL_LL_019_20160506144822.txt",)
    line=fr.readline()
    lineArr=line.strip().replace("{","").replace("}","").replace("\"","").replace(":",",").split(',')
    #print len(lineArr)
    column=[]
    for i in range(len(lineArr)):
        if i%2==1:
            column.append(lineArr[i])
    #lines=fr.readlines();
    column=column[3:]
    print len(column)
    return column
def loadDataValue(prefix,column,datafile):
    valcount=[]
    for i in range(len(column)):
        keyset={}
        valcount.append(keyset)
    fr=open(prefix+datafile)
    lines=fr.readlines()
    remaincol={}
    previousvalues=[]
    for k in range(0,1400):
        rowvalues=[]
        lineArr=lines[k].strip().replace("{","").replace("}","").replace("\"","").replace(":",",").split(',')
        for i in range(len(lineArr)):
            if i>6 and i%2==0:
                rowvalues.append(float(lineArr[i]))
        previousvalues.append(rowvalues)
                
    previousvalues=np.mat(previousvalues)       
    for k in range(1400,1500):
        lineArr=lines[k].strip().replace("{","").replace("}","").replace("\"","").replace(":",",").split(',')
    
        '''
        j:index of columns and values,since both of them are part of lineArr
        '''
        j=-1
        #print len(valcount)
        for i in range(len(lineArr)):
            if i>6 and i%2==0:
                j+=1
                if k==1400:
                    colpreval=[s[0] for s in previousvalues[:,j].getA().tolist()]
                
                keyset=valcount[j]
                
                if  lineArr[i] not in keyset:
                    keyset[lineArr[i]]=1
                    maxv=float(max(colpreval))
                    minv=float(min(colpreval))   
                    val=float(lineArr[i])
                    if (val<minv or val>maxv) :
                        colpreval.append(val)
                        if k==1498 or k==1499:
                            continue
                        print "col: %s" % column[j]
                        print "max: %f" % maxv
                        print "min: %f" % minv
                        print "val: %f" % float(lineArr[i])
                       
                        if column[j] in remaincol:
                            print column[j]
                            print k
                            remaincol[column[j]].append(k)
                        else:
                            remaincol[column[j]]=[]
                            remaincol[column[j]].append(k)
                else:
                    keyset[lineArr[i]]=int(keyset.get(lineArr[i]))+1
    removecol=[]
    for i in range(len(valcount)):
        for k,v in valcount[i].iteritems():
            if v==100:
                removecol.append(column[i])
            #if v==1:
                #remaincol.append(column[i])
   # print valcount
    '''
    for s in removecol:
        column.remove(s)
    print len(column)
    '''
    return removecol,remaincol
s="0.99"
#print s.find("^[0-9]")

def loadFileData(frf,fwf):
    column=loadColumn()
    fw=open(fwf,'w')
    datafiles= os.listdir(frf) 
    remaincolumns=[]
    removecolumns=[]
    for datafile in datafiles:
        print datafile
        removecolumn,remaincol=loadDataValue(frf,column,datafile)
        remaincolumn=[]
        for k,v in remaincol.iteritems():
            fw.write(k+' ')
            for s in v:
                fw.write(str(s)+' ')
            remaincolumn.append(k)
        fw.write("\n")
        
    #print remaincolumns
''''    
    tmpremainu=remaincolumns[0]
    tmpremaini=remaincolumns[0]
    tmpremove=removecolumns[0]
    print tmpremainu
    for i in range(1,len(remaincolumns)):
        
        print i
        print 'single remain columns: %s' %remaincolumns[i]
        print '------------------------------'
        
        removecolumn=list(set(tmpremove).union(set(removecolumns[i])))
        remaincolumnu=list(set(tmpremainu).union(set(remaincolumns[i])))#[val for val in tmpremain if val in remaincolumns[i]]#list(set(tmpremain).intersection(set(remaincolumns[i])))
        remaincolumni=list(set(tmpremaini).intersection(set(remaincolumns[i])))
        #print remaincolumn
        tmpremainu=remaincolumnu
        tmpremaini=remaincolumni
        tmpremove=removecolumn
   
    conflictcolumn=list(set(tmpremainu).intersection(set(tmpremove)))
    fw.write("conflictcolumns:\n")
    for s in conflictcolumn:
        fw.write(s+"\t")
    fw.write("\n")
    tmpremainu=list(set(tmpremainu)^set(conflictcolumn))
    tmpremove=list(set(tmpremove)^set(conflictcolumn))
    fw.write("tmp remain of union:\n")
    for s in tmpremainu:
        fw.write(s+"\t")
    fw.write("\n")
    fw.write("tmp remain of intersection:\n")
    for s in tmpremaini:
        fw.write(s+"\t")
    fw.write("\n")
    
    columnsinall=list(set(tmpremainu).union(set(tmpremove)))
    
    print conflictcolumn
    print len(tmpremainu)
    print tmpremainu
    print len(tmpremove)
    print tmpremove
    print len(columnsinall)
    print columnsinall
    '''
    
    


loadFileData("./data/","./20160829.txt")  

''' 
a=['ICon.Sta', 'ConTotCur3', 'ConTotCur1', 'ConTotCur2', 'WinSpe', 'VibSenNon', 'IGenHeaCot', 'XVibDri', 'HubSta', 'PlcSta', 'standard_state', 'CheHubBa2', 'CheHubBa1', 'YawAut', 'NacPosIni', 'IBar', 'ConPow', 'ConRotCur', 'XVibNon', 'VibSenDri', 'HubBusVo1', 'HubBusVo3', 'HubBusVo2', 'SafChaSta', 'ConGriCur1', 'HubFai002'] 
b=['HubBatVo3', 'ICon.Sta', 'ConTotCur3', 'ConTotCur1', 'ConTotCur2', 'WinSpe', 'IGenHeaCot', 'XVibDri', 'HubSta', 'PlcSta', 'standard_state', 'CheHubBa2', 'CheHubBa1', 'YawAut', 'NacPosIni', 'IBar', 'ConPow', 'ConRotCur', 'XVibNon', 'VibSenDri', 'IGeaFanCot', 'HubBusVo1', 'HubBusVo3', 'HubBusVo2', 'SafChaSta', 'ConGriCur1', 'HubFai002']
tmp=[val for val in a if val in b]
print tmp



tmp = [val for val in a if val in b]
print tmp
'''