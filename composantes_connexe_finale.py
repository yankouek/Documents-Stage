#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:33:44 2017

@author: znsc5162
"""
composante1=[]
composante2=[]
fichier1=open("composante_connexe_droite.txt","r")
for line in fichier1:
    composante1.append(int(line.split()[1]))
fichier1.close()


fichier2 = open("composante_connexe_gauche.txt","r")
for line in fichier2:
    composante2.append(int(line.split()[1]))
fichier2.close()

    
composante_finale=list(set().union(composante1,composante2))

print(len(composante1))
print(len(composante2))
print(len(composante_finale))

#print(composante_finale[0:100])

composante_finale_mots=[]
print(max(composante_finale))
fichier3= open("positions_mots.txt","r")
compt=0
intermed= []
for line in fichier3:
    compt=compt+1
    if compt < 2428:
        intermed.append(line.split()[0])
for val in composante_finale:
    composante_finale_mots.append(intermed[val])

print(composante_finale_mots[1750:1775])
fichier3.close()


