# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:35:35 2016

@author: jennychan
"""

import numpy as np
'''
#m=[[2,6,12,20],[6,20,42,72],[12,42,90,156],[20,72,156,272]]
m=[[30,100],[100,354]]
m=np.mat(m)
a,b=np.linalg.eig(m)
print a
print b

'''
n=[[1,1 ,1 ,0, 0],
[3 ,3 ,3 ,0 ,0],
[4,4,4,0,0],
[5,5,5,0,0],
[0 ,0, 0 ,4 ,4],
[0, 0 ,0 ,5 ,5],
[0 ,0 ,0 ,2 ,2],
[0,3,0,0,4]
]
m=[[0,3,0,0,4]]
#n=[[0,3,0,0,4],[0,2,0,0,5]]
m=np.mat(m)
print m
n=[[3,3],[4,4]]
n=np.mat(n)
U,sigma,V=np.linalg.svd(n,full_matrices=1)
print U
print 'bbbbbbbbbb'
print sigma
print V
print np.diag(1/sigma)
W=[[ 0.14142136 ,0 ],[0,0]]
W=np.mat(W)
q=V.T*W*W*U.T
print q
