#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:17:34 2017

@author: znsc5162
"""

import numpy as np 


M1=np.load("cooccurrences_finales_Droit_corr.npy")
M2=np.load("cooccurrences_finales_Gauche_corr.npy")


v=np.load("etat_stationnaire_mixte.npy")

s= range(3152)


index_mots=[]
with open("composante_connexe_finale.txt") as f1:
    for line in f1:
        val=line.split()
        index_mots.append(val[0])
      
        
        
def cat(mot):
    cat =mot[len(mot)-4:len(mot)-1]
    return(cat) 
    

    








def extraction_freq(phrase):
    Mat=np.zeros((len(phrase),len(phrase)))
    for i in range(len(phrase)):
        mot1=phrase[i]
        i1= index_mots.index(mot1)
        for j in range(len(phrase)):
            
            mot2=phrase[j]
            j1=index_mots.index(mot2)
            if i<=j:
                Mat[i][j]=M1[i1][j1]       
            else:    
                Mat[i][j]=M2[i1][j1]
            if Mat[i][j] < 1:
                Mat[i][j]=0
            if cat(mot2)=='ADV'     and   i==j+1:
                if Mat[i][j] == 0:
                    Mat[i][j]= 10
                
    return(Mat)
        
def extraction_mat_phrase(phrase):
    Mat=np.zeros((len(phrase),len(phrase)))
    for i in range(len(phrase)):
        mot1=phrase[i]
        i1= index_mots.index(mot1)
        for j in range(len(phrase)):
            mot2=phrase[j]
            j1=index_mots.index(mot2)
            if i<=j :
                if M1[i1][j1] < 1:
                     Mat[i][j]=0
                else:
                    Mat[i][j]=M1[i1][j1]/5**(abs(i-j))  
            else:  
                if M2[i1][j1] < 1:
                    Mat[i][j]=0
                else:
                    Mat[i][j]=M2[i1][j1]/5**(abs(i-j))     
            if i1==j1 and i!=j:
                 Mat[i][j]=0
            if cat(mot1)in ['DET','PRP'] and cat(mot2)=='NOM':
                  Mat[i][j]=0
            if cat(mot2) in ['DET','PRP'] and i<j:
                  Mat[i][j]=0
            if cat(mot2)  =='DET' and abs(i-j)>1:
                  Mat[i][j]=0
            if cat(mot2) == 'PRP'  and abs(i-j)>2:
                  Mat[i][j]=0
            if cat(mot2)=='NOM' and  cat(mot1) not in ['NOM','VER'] :
                  Mat[i][j]=0             
            if cat(mot1)==cat(mot2) and cat(mot2)not in ['NOM','VER','NPR'] and i!=j:
                  Mat[i][j]=0
            if cat(mot2) in ['ADV','PRN','DET']    and   i==j+1:
                Mat[j][i]=0
                if Mat[i][j] == 0:
                    Mat[i][j]= 1
                    
            if (cat(mot2)=='VER' and cat(mot1) not in ['VER']):
                 Mat[i][j]=0
                 
           
    for i in range(len(Mat)):
        s=sum(Mat[i])
        if s!=0:
            for j in range(len(Mat)):
                Mat[i][j]=Mat[i][j]/s
        else:
            print(str(i),"n'est lie a personne" )
    return(Mat)
            
def extraction_Proba(phrase):
    P=np.zeros((1,len(phrase)))
    for i in range(len(phrase)):
        mot1=phrase[i]
        i1= index_mots.index(mot1)
        P[0][i]=v[0][i1]
    return(P)
    



 
def passage_v_w(P):
    P2=[]
    for i in range(len(P[0])):
        P2.append(P[0][i])
    P3=sorted(P2,reverse=True)
   
    P4=np.zeros((1,len(P[0])))
    for i in range(len(P[0])):
       P4[0][i]=P3[i]
    return(P4)
    
def sigmam1(P):
    sigmam1=[]
    plist=[]
    for compt in range(len(P[0])):
        plist.append(P[0][compt])
    
    for compt1 in range(len(P[0])):
        valeur=(passage_v_w(P))[0][compt1]
        sigmam1.append(plist.index(valeur))
    return(sigmam1)

def construct_K(phrase):
    K=np.zeros((len(phrase),len(phrase)))
    P= extraction_Proba(phrase)
    Mat1=extraction_mat_phrase(phrase)
    sigmamoins=sigmam1(P)
    
    for l in range(len(phrase)) :
            Mat1[l][l]=(len(phrase)-1)/(len(phrase))
 
    for val in range(len(phrase)): 
        i=sigmamoins[val]
        reste=1
        sigma=0
        
        for j in range(len(phrase)):
            if K[i][j]!=0:
                reste=reste-K[i][j]
            else:
                 sigma=sigma+Mat1[i][j]
        for j2 in range(len(phrase))  :
            if Mat1[i][j2]!=0 and K[i][j2]==0:
                K[i][j2]=(Mat1[i][j2]*reste)/sigma
                K[j2][i]=((K[i][j2])*P[0][j2])/P[0][i]
                
                
    return(K)
                


def sym(phrase):
    K=construct_K(phrase)
    S=K*0
    P= extraction_Proba(phrase)
    for  i in range(len(phrase)):
        for j in range(len(phrase)):
            if K[i][j]!=0:
                S[i][j]=K[i][j]/P[0][i]
    return(S)
                
phrase1 = ['(je,PRN)','(chercher,VER)','(un,DET)','(vol,NOM)', '(pour,PRP)', '(paris,NPR)', '(via,PRP)', '(berlin,NPR)']
 
print(phrase1)




Mat_adjac= sym(phrase1)
Mat_proba = construct_K(phrase1)
test = extraction_freq(phrase1)
def ecrire_matrice(nom,M,f):
    f.write(nom)
    f.write(":  \n")
    for i in range(len(M)):
        for j in range(len(M[i])):
            f.write(str(M[i][j])[0:5] + "  ")
        f.write("\n")
    f.write("  \n")
    

Mat_prob=extraction_mat_phrase(phrase1)
            
if __name__ == '__main__':
        print("Matrice_frequence:  \n", extraction_freq(phrase1),"\n")
        print("matrice_proba: \n", extraction_mat_phrase(phrase1),"\n")
        #print("probabilites : \n ", extraction_Proba(phrase1),"\n")
        print("Matrice_des_probabilités_conditionelles : \n",construct_K(phrase1),"\n")
 
        print(Mat_adjac)


    