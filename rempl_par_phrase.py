#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:02:52 2017

@author: znsc5162
"""


ouvert = open("nom_fic")
conteneur=ouvert.read().splitlines()
    
for fichier in conteneur:    
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
        
        
        
        
        G = open(fichier)
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
        
        #print(len(noeuds_text(fichier))) 
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
        
        
        
        
        def dominance_droite(P):
                domdroit= open("dominance_droite.txt", "a")
                for val1 in range(len(P)) :
                     
                     for val2 in range(len(P)):
                        if val1 != val2:
                            carac="("+P[val1][0]+","+P[val1][1]+")"+"      "+ "("+P[val2][0]+","+P[val2][1]+")"
                            if P[val1][1]=='VER' and P[val2][1]=='NOM' and val2 <val1+4:
                               domdroit.write(carac +" \n")
                            elif P[val1][1]=='VER' and P[val2][1]=='NPR' and val2<val1+2:
                                domdroit.write(carac+" \n")
                            elif P[val1][1]=='VER' and P[val2][1]=='CON' and val2<val1+2:
                                domdroit.write(carac+" \n")
                            elif P[val1][1]=='CON' and P[val2][1] in ['NOM','NUM','DAT','NPR','VER']:
                                domdroit.write(carac+" \n")
                            elif P[val1][1]=='NOM' and P[val2][1]=='ADJ' and val2==val1+1:
                             domdroit.write(carac+" \n")
                            
                            elif P[val1][1]=='NUM' and P[val2][1]=='DATEM' :
                               domdroit.write(carac+" \n")
                             
                            elif P[val1][1]=='PRP' and P[val2][1] in ['NOM','NUM','DAT','NPR'] and val2==val1+1:
                               domdroit.write(carac+" \n")
                            elif P[val1][1]=='VER' and P[val2][1]=='ADJ' and val2==val1+1:
                              domdroit.write(carac+" \n")
                            elif P[val1][1]=='VER' and P[val2][1]=='ADV' and val2==val1+1:
                               domdroit.write(carac+" \n")
                            elif (P[val1][1],P[val2][1]) not in [('DET','NOM'),('ADV','ADJ'),('ADJ','VER'),('NOM','VER'),('VER','ADJ'),('DET','VER')] and  val2 <= val1+2 :
                               domdroit.write(carac+" \n")
                domdroit.close() 
                
                
                
                
                
        def dominance_gauche(P):
                domgauche= open("dominance_gauche.txt", "a")
                for val1 in range(len(P)) :
                     
                     for val2 in range(len(P)):
                         if val1 != val2:
                            carac="("+P[val1][0]+","+P[val1][1]+")"+"      "+ "("+P[val2][0]+","+P[val2][1]+")"
                            if P[val1][1]=='VER' and P[val2][1] in ['VER','PRN'] and  val2 > val1-2 :
                                    domgauche.write(carac+" \n")
                            elif P[val1][1]=='DET' and P[val2][1]=='NOM'and val2==val1-1:
                                    domgauche.write(carac+" \n")
                            elif P[val1][1]=='ADJ' and P[val2][1]=='ADV'and val2==val1-1:
                                    domgauche.write(carac+" \n")
                            elif P[val1][1]=='PRP' and P[val2][1] in ['NOM','NUM','DATEM','NPR'] and val2==val1-1:
                                   domgauche.write(carac+" \n")
                            elif P[val1][1]=='CON' and P[val2][1] in ['NOM','NUM','DAT','NPR'] and val2==val1-1:
                                  domgauche.write(carac+" \n")
                            elif (P[val1][1],P[val2][1]) not in [('VER','ADJ'),('NOM','DET'),('NPR','DET'),('VER','DET')] and  val2 >= val1-2 :
                                    domgauche.write(carac+" \n")
                domgauche.close()  
        phrases=decoup_phrase_list(fichier)
        compteur=0
        for phrase in phrases:
          compteur = compteur+1
          dominance_droite(phrase)
          dominance_gauche(phrase)
          if compteur%50000 ==0 :
              print(fichier,"phrase",compteur)

            