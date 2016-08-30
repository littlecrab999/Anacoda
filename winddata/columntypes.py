# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 19:51:24 2016

@author: liuyue
"""
import codecs
def splitcolumn(s):
    
    fr=open(s)
    lines=fr.readlines()
    columndict={}
    for line in lines:
        
        #print 'line %s' % line
        columns=line.split('\t')
        #print columns
        columntype=columns[2]
        column=columns[6]
        if columntype in columndict:
            columndict[columntype].append(column)
        else:
            columndict[columntype]=[]
            columndict[columntype].append(column)
    fw=open('./data/columns.txt','w')
    for k,v in columndict.iteritems():
        fw.write(k)
        fw.write(": ")
        fw.write(str(v))
        fw.write("\n")
    
    fr=open('./processedcolumns.txt')
    
    lines=fr.readlines()
    for i in range(8):
        columns=lines[i].split('\t')
        types=set()
        for column in columns:
            for k,v in columndict.iteritems():
                if column in v:
                    types.add(k)
        print types
        for s in types:
            fw.write(s+' ')
        fw.write("\n")
                    
    
    



splitcolumn(r'./data/columntypes.txt')