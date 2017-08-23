#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:50:49 2017

@author: znsc5162
"""

import numpy as np 

M1=np.load("cooccurrences_finales_Gauche_corr.npy")
M2=np.load("cooccurrences_finales_Droit_corr.npy")

M=np.transpose(M1+M2)

vect=np.zeros((1,3152))

for i in range(3152):
    vect[0][i]=1/3152
        
for i in range(3152):
    somme= sum(M[i])
    for j in range(3152):
        M[i][j]=M[i][j]/somme
val=vect

for i in range(150):
    val=np.dot(val,M)

print(val) 
np.save("etat_stationnaire_mixte.npy",val)        
         

