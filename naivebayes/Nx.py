# -*- coding: utf-8 -*-
"""
Created on Wed May 04 15:58:36 2016

@author: jennychan
"""

import networkx as nx

G=nx.Graph()
G.add_node(1,time='4pm')

nx.draw(G)