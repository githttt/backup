# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:40:54 2018

@author: sylar
"""

import numpy as np

def RepeatLine(a, b):
    X = np.loadtxt(a, delimiter=",")
    L = []
    D = []
    
    for i in range(len(X)-1):
        if(i <= len(X)-4):
            if((X[i]==X[i+1]).all()):
                if((X[i]==X[i+2]).all()):
                    L.append(i+1)
                    L.append(i+2)
                    L.append(i+3)
                elif((X[i]==X[i+3]).all()):
                    L.append(i+1)
                    L.append(i+2)
                    L.append(i+4)
                else:
                    continue
            elif((X[i]==X[i+2]).all()):
                if((X[i]==X[i+3]).all()):
                    L.append(i+1)
                    L.append(i+3)
                    L.append(i+4)
                else:
                    continue
        elif(i == len(X)-3):
            if((X[i]==X[i+1]).all()):
                if((X[i]==X[i+2]).all()):
                    L.append(i+1)
                    L.append(i+2)
                    L.append(i+3)
    
    for i in L:
        D.append(X[i-1])
    
    out = np.array(D)
    print(out.shape)
    
    np.savetxt(b, out, fmt='%.8e', delimiter = ',')
    
RepeatLine("originalData/spectre011.csv", 'repeat_011.csv')
RepeatLine("originalData/spectre012.csv", 'repeat_012.csv')
RepeatLine("originalData/spectre013.csv", 'repeat_013.csv')
RepeatLine("originalData/spectre014.csv", 'repeat_014.csv')