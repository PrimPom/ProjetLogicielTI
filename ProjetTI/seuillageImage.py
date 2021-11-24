# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:10:50 2019

@author: primp
"""

# Seuillage de l'image
"""
def seuillageImage(image,seuil):
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            
            if image[i][j] < seuil :
                
                image[i][j] = 0
            else :
                image[i][j] = 1
    
    return image"""
    

def seuillageImage(image,seuil):
    resultat = image.copy()
    s = image.shape
    for j in range(s[0]):
        for i in range(s[1]):
            if image[j][i] > seuil:
               resultat[j,i] = 1
            else:
                resultat[j,i] = 0
    return resultat