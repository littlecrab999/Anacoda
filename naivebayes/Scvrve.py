# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:54:37 2016

@author: jennychan
"""

import matplotlib.pyplot as plt


#ax1=plt.subplot(111)

sim=[]
s=0.1

for i in range(9):
    sim.append(s)
    print s
    s+=0.1
    
ran={3:10,6:20,5:50}
k=5
v=50
y=[]
for s in sim:
    p=1-(1-s**k)**v
    y.append(p)

plt.plot(sim,y)
    
'''
lv:5:50
hong:6:20
lan 3:10
'''


    
    