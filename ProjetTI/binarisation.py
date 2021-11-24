# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:31:11 2019

@author: primp
"""

def binarisation(image,histo,seuil):
    s = image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            if histo[i][j] > seuil :
                histo[i][j] = 0
            else :
                histo[i][j] = 1
    return histo