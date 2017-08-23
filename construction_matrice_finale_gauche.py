##!/u-r/bin/env python3
## -*- coding: utf-8 -*-
#"""
#Created on Mon Jun 19 16:17:14 2017
#
#@author: znsc5162
#"""

import numpy as np
import random as rdm
composante1=[]
composante2=[]
fichier1=open("composante_connexe_droite.txt","r", encoding="utf-8")
for line in fichier1:
    composante1.append(int(line.split()[1]))
fichier1.close()


fichier2 = open("composante_connexe_gauche.txt","r", encoding="utf-8")
for line in fichier2:
    composante2.append(int(line.split()[1]))
fichier2.close()

composante1.append(0)
    
composante_finale=list(set().union(composante1,composante2))

print(len(composante_finale))
print(max(composante_finale))




composante_finale_mots=[]

fichier3= open("positions_mots_new.txt","r", encoding="utf-8")
compt=0

intermed= []
for line in fichier3:
    compt=compt+1
    if compt < 3154:
        intermed.append(line.split()[0])
        
print(len(intermed)) 

compt=0
for val in composante_finale: 
    composante_finale_mots.append(intermed[val])
    compt=compt+1
fichier3.close() 

fichier4=open("composante_connexe_finale.txt","w")

for i in range(3152):
    fichier4.write(composante_finale_mots[i])
    fichier4.write("        ")
    fichier4.write(str(i)+"\n")
    
fichier4.close()
#
##
##
#
#
#
#
#
#
#
#cooc_Droit=np.zeros((len(composante_finale_mots), len(composante_finale_mots)))
#compt=0
#with open("dom_droit.txt", "r", encoding="utf-8")  as fichier4:
#    for line in fichier4:
#        v=line.split()
#        for mot in composante_finale_mots:
#            i=composante_finale_mots.index(mot)
#            if v[1]==mot:
#                for mot2 in composante_finale_mots:
#                    if v[2]==mot2:
#                        j=composante_finale_mots.index(mot2)
#                        cooc_Droit[i][j]=v[0]
#                        print(i,j,v[0])
#                        compt=compt+1
#                        if compt%1000==0:
#                            print("coeff",compt)
#                        break
#    
#        
#          
#vect=np.zeros((1,3152))
#for compt in range(3152):
#    vect[0][compt]=1/3152
#        
#v=np.load("cooccurrences_finales_Droit_bis.npy")
#for i in range(3152):
#    somme=sum(v[i])
#    for j in range(3152):
#       v[i][j]=v[i][j]/somme
#np.save("cooccurrences_finales_Droite_stochastique.npy",v)     
#
#val=vect
#for i in range(120):
#    val=np.dot(val,v)
#    #print(val[0][2000:2100])
#    
#print(val)  
# 
#np.save("etat_stationnaire_Droit.npy",val)
 
#        
#
#np.save("cooccurrences_finales_Droit.npy",cooc_Droit)
#
#for i in range(3152):
#    for j in range(3152):
#        cooc_Droit[i][j]=int(cooc_Droit[i][j])
     
     
#v=np.load("cooccurrences_finales_Droit.npy") #pour charger la matrice plus tard 
#ne pas oublier de faire int des valeurs

