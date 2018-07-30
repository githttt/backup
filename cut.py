# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:02:48 2018

@author: sylar
"""

import numpy as np

def CutRepeat(a, b):
    X = np.loadtxt(a, delimiter=",")
    L = []
    D = []
    
    for i in range(len(X)-1):
        if(i <= len(X)-2 and i >= i):
            if((X[i]==X[i+1]).all()):
                continue
            elif((X[i]==X[i-1]).all()):
                continue
            else:
                L.append(i+1)
        else:
            L.append(i+1)
    
    for i in L:
        D.append(X[i-1])
    
    out = np.array(D)
    print(out.shape)
    
    np.savetxt(b, out, fmt='%.8e', delimiter = ',')
    
CutRepeat("originalData/spectre011_25.csv", 'cutrepeat3_011.csv')
CutRepeat("originalData/spectre012_25.csv", 'cutrepeat3_012.csv')
CutRepeat("originalData/spectre013_25.csv", 'cutrepeat3_013.csv')
CutRepeat("originalData/spectre014_25.csv", 'cutrepeat3_014.csv')
