#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 15:57:45 2017

@author: znsc5162
"""
import numpy as np
M1=np.load("cooccurrences_finales_Droit.npy")
M2=np.load("cooccurrences_finales_Gauche.npy")


def trans_matrice_proba(M):
    N=len(M)
    renvoi=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            try:
                renvoi[i][j]=int(M[i][j])/int(sum(M[i]))
            except ZeroDivisionError:
                print(i)
                break 
    return(renvoi)

v= trans_matrice_proba(M1)