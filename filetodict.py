#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:37:36 2017

@author: znsc5162
"""

#from collections import defaultdict
#cette version des fonctions de comptage inclut 
#toutes les differences de garmmaires entre  le fichier d'etiqutege et celui de lemmatisation 


def mot_to_lemme(filemme):
  G1 = open(filemme)
  f1=G1.readlines()
  d={}
  d={(line.split()[0],line.split()[4][0:3]):line.split()[1] for line in f1}
  G1.close()
  return(d)


liste_lemme=mot_to_lemme("lemme")


#print(liste_lemme)


def trans_noeuds_text(v):
    for i in range(len(v)) :
        if v[i] in liste_lemme.keys():
            v[i]=(liste_lemme[v[i]],v[i][1])
    return(v)





 
#renvoie les noeuds du texte (ie: les couples mots_catégorie grammaticale)
def noeuds_text(file):
  G = open(file)
  f=G.read()
  G.close()
  a=f.split()
  v=[]
  for i in range(0,len(a),2):
      if a[i+1]!='PUN' and a[i+1]!='APOS'and a[i+1]!='PUN:cit':
          if len(a[i+1])>3 and a[i+1][3]==':':
              if a[i+1][0:3]=='PRO':
                  v.append((a[i],'PRN'))
              else:
                  v.append((a[i],a[i+1][0:3]))
                  
          else:
              v.append((a[i],a[i+1]))
  U=set(trans_noeuds_text(v))
  return(U)

#print(len(noeuds_text(fichier_etiquete))) 
#compte le nombre de chaque noeud mot catégorie grammaticale on 
#a la ponctuation en plus maisq
#pas grave les noeuuds sont des clés de
# dictionnaire on peut les rechercher facilement si on les ecrit
#bien


    #compte les occurences de chaque couple mot catégories 
def count_noeuds(file):
  noeuds=noeuds_text(file)
  G = open(file)
  f=G.read()
  G.close()
  a=f.split()
  v=[]
  for i in range(0,len(a),2):
     if a[i+1]!='PUN' and a[i+1]!='APOS'and a[i+1]!='PUN:cit':
          if len(a[i+1])>3 and a[i+1][3]==':':
              if a[i+1][0:3]=='PRO':
                  v.append((a[i],'PRN'))
              else:
                  v.append((a[i],a[i+1][0:3]))
                  
          else:
              v.append((a[i],a[i+1]))
  v=trans_noeuds_text(v)
  u =[0]*len(noeuds)
  compt=0
  noeuds_bis=[]
  for val in noeuds:
      for j in range(len(v)):
          if v[j]==val: 
              u[compt]=u[compt]+1
      compt=compt+1
      noeuds_bis.append(val)
  d={noeuds_bis[i]:u[i] for i in range(len(noeuds))}

  return(d)

#print(count_noeuds(fichier_etiquete))



#proba d'un noeud schant un autre :
    
def proba_absolue_noeud(noeud,file):
    return(count_noeuds(file)[noeud]/len(noeuds_text(file)))

#print(proba_absolue_noeud(('obama', 'PATRO'),fichier_etiquete))



#decoupe le fichier etiquté en phrases 
def decoup_phrase_list(file):
    G = open(file)
    f=G.read()
    G.close()
    a=f.split()
    v=[]
    for i in range(0,len(a),2):
        if a[i+1]!='PUN' and a[i+1]!='APOS'and a[i+1]!='PUN:cit':
             if len(a[i+1])>3 and a[i+1][3]==':':
              if a[i+1][0:3]=='PRO':
                  v.append((a[i],'PRN'))
              else:
                  v.append((a[i],a[i+1][0:3]))
                  
             else:
              v.append((a[i],a[i+1]))
    v=trans_noeuds_text(v)
    P=[]
    phrases=[]
    for k in range(len(v)) :
        if v[k] != ('.', 'SENT'):
            P.append(v[k])
        else:
            P.append(('.', 'SENT'))
            phrases.append(P)
            P=[]
    return(phrases)


#print(decoup_phrase_list(fichier_etiquete))  
#a refaire


def proba_sachant_j_plus(noeud1,noeud2,dist):
 
  l=[]
  if noeud1 in count_noeuds(fichier_etiquete).keys():
      for i in range(len(v)):
          if v[i]==noeud1:
              l.append(i)
              compt=0
              for j in l:
                  if j+dist<=len(v)-1 and ('.','sent') not in v[j:j+dist] and ('?','sent') not in v[j:j+dist]:
                      if v[j+dist]==noeud2:
                          compt=compt+1
      return(compt/count_noeuds(fichier_etiquete)[noeud1],compt)
  else:
     return(0,0)
     



#print(proba_sachant_j_plus(('avoir', 'VER'),('de', 'PRP'),fichier_etiquete,1))



def proba_sachant_j_moins(noeud1,noeud2,dist):
  l=[]
  if noeud1 in count_noeuds(fichier_etiquete).keys():
      for i in range(len(v)):
          if v[i]==noeud1:
              l.append(i)
              compt=0
              for j in l:
                  if j-dist >= 0 and ('.','sent') not in v[j-dist:j] and ('?','sent') not in v[j-dist:j] :
                      if v[j-dist]==noeud2:
                          compt=compt+1
                  
      return(compt/count_noeuds(fichier_etiquete)[noeud1],compt)
  else:
     return(0,0)
     



#print(proba_sachant_j_plus(('à','PRP'),('côté','NOM'),fichier_etiquete,1))

#pour 240000 (entité-catégories) soit environs 16000 (mots-categories)
#n retitant la ponctuation on commence à avoir des resultats accptables ,
# les temps de compilations eux sont d'environ 22-25 minutes pour le calcul d'une coocurence
#il faudrait penser à réduire ce temps soit en distribuant la tache soit en 
 #augmentant la puissance de la machine 
def coocurence_plus(cat1,cat2,file,dist):
  l=[]
  for i in range(len(v)):
      if v[i][1]==cat1:
          l.append(i)
  compt=0
  for j in l :
      if j+dist <= len(v)-1 and ('.','sent') and ('.','sent') not in v[j:j+dist] and ('?','sent') not in v[j:j+dist]:
          if v[j+dist][1]==cat2:
              compt=compt+1
  return(compt/(len(l)+(len(l)==0)),compt)     
  
#for k in [1,2,3]:
    #print(coocurence_plus('DET','NOM',fichier_etiquete,k))




def coocurence_moins(cat1,cat2,dist):
  
  l=[]
  for i in range(len(v)):
      if v[i][1]==cat1:
          l.append(i)
  compt=0
  for j in l:
      if j-dist >= 0 and ('.','sent') and ('.','sent') not in v[j-dist:j] and ('?','sent') not in v[j-dist:j]:
          if v[j-dist][1]==cat2:
              compt=compt+1
  return(compt/(len(l)+(len(l)==0)),compt)  


#dominant à gauche , dominé à une certaine porté plus loin devant  :
def phrase_to_matrice(P):
  M1=[]
  for val1 in range(len(P)) :
      M1.append([0]*len(P))
  for val1 in range(len(P)) :
        for val2 in range(len(P)):
            if val1==val2:
                M1[val1][val2]=0
            elif P[val1][1]=='VER' and P[val2][1]=='NOM':
                for decompt in [1,2,3,4,5]:
                      M1[val1][val2]= M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],decompt)[1]
            elif P[val1][1]=='SENT':
                M1[val1][val2]=0
                  
            elif P[val1][1]=='DET' and P[val2][1]=='NOM'and val2==val1+1:
             M1[val1][val2]= M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
            
            elif P[val1][1]=='NOM' and P[val2][1]=='ADJ' and val2==val1+1:
                M1[val1][val2]= M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
            
            elif P[val1][1]=='NUM' and P[val2][1]=='DATEM'and val2==val1+1:
                M1[val1][val2]=M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
             
            elif P[val1][1]=='PRP' and P[val2][1] in ['NOM','NUM','DATEM','NPR'] and val2==val1+1:
                 M1[val1][val2]=M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
            elif P[val1][1]=='VER' and P[val2][1]=='VER' and val2==val1+1:
                M1[val1][val2]=M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
            else:
                for decompt2 in [1,2]:
                     M1[val1][val2]= M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],decompt2)[1]
  return(M1)


#dominant à droite dominé à une certaine portée plus loin derriere:
    

def phrase_to_matrice_sym(P):
  M1=[]
  for val1 in range(len(P)) :
      M1.append([0]*len(P))
  for val1 in range(len(P)) :
        for val2 in range(len(P)):
            if val1==val2:
                M1[val1][val2]=0
            elif P[val2][1]=='VER' and P[val1][1]=='NOM':
                for decompt in [1,2,3,4,5]:
                      M1[val1][val2]= M1[val1][val2]+proba_sachant_j_moins(P[val1],P[val2],decompt)[1]
            elif P[val1][1]=='SENT':
                M1[val1][val2]=0
            elif P[val2][1]=='DET' and P[val1][1]=='NOM':
             M1[val1][val2]= M1[val1][val2]+proba_sachant_j_plus(P[val1],P[val2],1)[1]
           
            else:
                for decompt2 in [1,2,3]:
                     M1[val1][val2]= M1[val1][val2]+proba_sachant_j_moins(P[val1],P[val2],decompt2)[1]
  return(M1)

    











fichier_etiquete= "etiquete1.txt"
G = open(fichier_etiquete)
f=G.read()
G.close()
a=f.split()
v=[]
for i in range(0,len(a),2):
   if a[i+1]!='PUN' and a[i+1]!='APOS'and a[i+1]!='PUN:cit':
            if len(a[i+1])>3 and a[i+1][3]==':':
                if a[i+1][0:3]=='PRO':
                    v.append((a[i],'PRN'))
                else:
                    v.append((a[i],a[i+1][0:3]))
                  
            else:
                v.append((a[i],a[i+1]))
v=trans_noeuds_text(v)

P=[('le', 'DET'), ('etats', 'NPR'), ('unis', 'NPR'), ('avoir', 'VER'), ('surmonter', 'VER'), ("l'", 'DET'), ('esclavage', 'NOM'), ('le', 'DET'), ('guerre', 'NOM'), ('civil', 'ADJ')]



M=phrase_to_matrice(P)
for val in ["etiquete2.txt","etiquete3.txt","etiquete4.txt","etiquete5.txt","etiquete6.txt","etiquete7.txt","etiquete8.txt","etiquete9.txt","etiquete10.txt"]:
    fichier_etiquete = val
    G = open(fichier_etiquete)
    f=G.read()
    G.close()
    a=f.split()
    v=[]
    for i in range(0,len(a),2):
          if a[i+1]!='PUN' and a[i+1]!='APOS'and a[i+1]!='PUN:cit':
              if len(a[i+1])>3 and a[i+1][3]==':':
                  if a[i+1][0:3]=='PRO':
                    v.append((a[i],'PRN'))
                  else:
                    v.append((a[i],a[i+1][0:3]))
                  
              else:
                v.append((a[i],a[i+1]))
    v=trans_noeuds_text(v)
 

    M1=phrase_to_matrice(P)
    for i in range(len(M)):
       for j in range(len(P)):
            M[i][j]=M1[i][j]+M[i][j]



print(M)




#print("commentaire important: ici les couples qui ne match (les litigieux) ne valent en fait pas la peine d'être lemmatisés")

#reste à pouvoir compter les dépendances de gauche vers droite 
