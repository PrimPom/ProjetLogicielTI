# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:17:47 2019

@author: primp
"""

def aminciHuConnexite(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and (Image[ligne-1,colonne]==1) and  (Image[ligne-1,colonne+1]==1):
                #ligne du bas
                if (Image[ligne+1,colonne-1]==0) and (Image[ligne+1,colonne]==0) and  (Image[ligne+1,colonne+1]==0):
                    #ligne actuelle
                    if Image[ligne,colonne]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLun(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and (Image[ligne-1,colonne]==1) :
                #ligne du bas
                if  (Image[ligne+1,colonne]==0) and  (Image[ligne+1,colonne+1]==0):
                    #ligne actuelle
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==0:
                        resultat[ligne,colonne]=0
               
    return resultat


def aminciLdeux(Image):
    s = Image.shape
    resultat = Image
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and (Image[ligne-1,colonne+1]==0) :
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==1) and  (Image[ligne+1,colonne+1]==0):
                    #ligne actuelle
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==0:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLtrois(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne]==0) and (Image[ligne-1,colonne+1]==0) :
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==1) and  (Image[ligne+1,colonne]==1):
                    #ligne actuelle
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==0 :
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLquatre(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==0) and Image[ligne-1,colonne]==0 and (Image[ligne-1,colonne+1]==0) :
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==1) and  (Image[ligne+1,colonne]==1) and Image[ligne+1,colonne+1]==1:
                    #ligne actuelle
                    if Image[ligne,colonne]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLcinq(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==0) and Image[ligne-1,colonne]==0:
                #ligne du bas
                if  (Image[ligne+1,colonne]==1) and Image[ligne+1,colonne+1]==1:
                    #ligne actuelle
                    if Image[ligne,colonne-1]==0 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLsix(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==0) and Image[ligne-1,colonne+1]==1:
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==0) and Image[ligne+1,colonne+1]==1:
                    #ligne actuelle
                    if Image[ligne,colonne-1]==0 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciLsept(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne]==1) and Image[ligne-1,colonne+1]==1:
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==0) and Image[ligne,colonne]==0:
                    #ligne actuelle
                    if Image[ligne,colonne-1]==0 and Image[ligne,colonne]==1 and Image[ligne,colonne+1]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def tourCompletAminci(Image):
    
    resultat = aminciLsept(aminciLsix(aminciLcinq(aminciLquatre(aminciLtrois(aminciLdeux(aminciLun(aminciHuConnexite(Image))))))))
   
               
    return resultat

def homothopique(Image,nombreIte):
    resultat = tourCompletAminci(Image)
    resultatSuivant=tourCompletAminci(resultat)
    
    """while (resultatSuivant == resultat).all() :
        #tampon=resultatSuivant
        resultat=resultatSuivant
        resultatSuivant=tourCompletAminci(resultat)"""
    for i in range(nombreIte):
        resultat=tourCompletAminci(resultatSuivant)
        resultatSuivant=resultat
      
    return resultat