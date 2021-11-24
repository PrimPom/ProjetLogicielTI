# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:35:34 2019

@author: primp
"""

def dilatationImage(Image):
    s = Image.shape
    resultat = Image.copy()
    for i in range(1,s[0]-2):
        for j in range(1,s[1]-2):
            somme=0;
            for k in range(-1,2):
                for l in range(-1,2):
                       somme=somme+Image[i+k,j+l]
            if somme>=1 :
                    resultat[i,j]=1
            #else :
                    #resultat[i,j]=0
    
    
    
    return resultat