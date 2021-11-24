# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:26:40 2019

@author: primp
"""

def additionImage(image1,image2):
    resultat = image1.copy()
    sizeImage1 = image1.shape
    sizeImage2= image2.shape
    if(sizeImage1[0]==sizeImage2[0] and sizeImage1[1]==sizeImage2[1] ) :
        for j in range(sizeImage1[0]):
            for i in range(sizeImage1[1]):
                if image1[j,i]+image2[j][i]>=1:
                    resultat[j,i]=1
                    #print(resultat[j,i])
                else:
                    resultat[j,i] = 0
    else :
        print("Les deux image ne sont pas de meme tai")
    
    return resultat