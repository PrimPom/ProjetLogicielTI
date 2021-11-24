# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:49:01 2019

@author: primp
"""

def histogramme(image):
    h = np.zeros(256,dtype=np.float32)#tableau de 256 elmts intialiser à 0 de typtr dtype: float32
    s = image.shape#récupérer la taille de l'image grâce à la fonction shape
    for j in range(s[0]):
        for i in range(s[1]):
            valeur = image[j,i]
            print(valeur)
            #h[valeur] += 1
    return h