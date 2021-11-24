# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:59:31 2019

@author: primp
"""
from additionImage import additionImage
from soustractionImage import soustractionImage
from ouvertureImage import ouvertureImage
def erosionUnite(Image):
    s = Image.shape
    resultat = Image.copy()
    for i in range(1,s[0]-2):
        for j in range(1,s[1]-2):
            somme=0;
            for k in range(-1,2):
                for l in range(-1,2):
                       somme=somme+Image[i+k,j+l]
            if somme==9 :
                    resultat[i,j]=1
            else :
                    resultat[i,j]=0                  
    return resultat

def erosion(Image,u,v,S):
    s = Image.shape
    resultat = Image.copy()
    for i in range(u,s[0]-v):
        for j in range(u,s[1]-v):
            somme=0;
            for k in range(-u,v):
                for l in range(-u,v):
                       somme=somme+Image[i+k,j+l]
                       #print(somme)
            if somme==S :
                    resultat[i,j]=1
                    #print(somme)
            else :
                    resultat[i,j]=0                  
    return resultat

def dilatation(Image,u,v):
    s = Image.shape
    resultat = Image.copy()
    for i in range(u,s[0]-v):
        for j in range(u,s[1]-v):
            somme=0;
            for k in range(-u,v):
                for l in range(-u,v):
                       somme=somme+Image[i+k,j+l]
            if somme>=1 :
                    resultat[i,j]=1
            #else :
                    #resultat[i,j]=0
       
    return resultat

def lantuejoulHuConnexite(Image):
    u=2
    v=3
     
    squelettePrec=soustractionImage(erosionUnite(Image),ouvertureImage(erosionUnite(Image)))
    squelette_lantuejoul=soustractionImage(erosion(Image,u,v,(u+v)**2),ouvertureImage(erosion(Image,u,v,(u+v)**2)))
    sommeImagePrec=additionImage(squelettePrec,squelette_lantuejoul)
    u=u+1
    v=v+1
    squelette_LANTUEJOULE=soustractionImage(erosion(Image,u,v,(u+v)**2),ouvertureImage(erosion(Image,u,v,(u+v)**2)))
    sommeImageActuelle=additionImage(sommeImagePrec,squelette_LANTUEJOULE)

    
    """while (sommeImagePrec == sommeImageActuelle).all()==False :
        #tampon=resultatSuivant
        u=u+1
        v=v+1
        sommeImagePrec == sommeImageActuelle
        squelette_LANTUEJOULE=soustractionImage(erosion(Image,u,v,(u+v)**2),ouvertureImage(erosion(Image,u,v,(u+v)**2)))
        sommeImageActuelle=additionImage(sommeImagePrec,squelette_LANTUEJOULE)
      """
        
    for i in range(1):
        u=u+1
        v=v+1
        sommeImagePrec == sommeImageActuelle
        squelette_LANTUEJOULE=soustractionImage(erosion(Image,u,v,(u+v)**2),ouvertureImage(erosion(Image,u,v,(u+v)**2)))
        sommeImageActuelle=additionImage(sommeImagePrec,squelette_LANTUEJOULE)
      
    return sommeImageActuelle #ouvertureImage(erosion(Image,3,4, (3+4)**2))
