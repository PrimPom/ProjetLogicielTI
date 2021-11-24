# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:10:01 2019

@author: primp
"""
import numpy as np

def imageHexagonale(Image):
    taille=Image.shape
    imageHexa=np.zeros((taille[0],taille[1]+1))
    
    for i in range(0,taille[0]):
        if i%2==0:#ligne paire
            imageHexa[i][0]=0
            imageHexa[i,1:]=Image[i,:]
        else :
            imageHexa[i,:taille[1]]=Image[i,:]
            imageHexa[i,taille[1]]=0
            
    return imageHexa