# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:48:21 2019

@author: primp
"""

def aminciSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and Image[ligne-1,colonne]==1:
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==0) and Image[ligne+1,colonne]==0:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if  Image[ligne,colonne]==1 :
                        resultat[ligne,colonne]=0
               
    return resultat

def erosionDisque(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            somme=Image[ligne-1,colonne]+Image[ligne-1,colonne+1]+Image[ligne+1,colonne+1]+Image[ligne+1,colonne]+Image[ligne,colonne-1]+Image[ligne,colonne]+Image[ligne,colonne+1]
            if somme==7 :
                    resultat[ligne,colonne]=1
            else :
                    resultat[ligne,colonne]=0
               
    return resultat

def dilatationDisque(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            somme=Image[ligne-1,colonne]+Image[ligne-1,colonne+1]+Image[ligne+1,colonne+1]+Image[ligne+1,colonne]+Image[ligne,colonne-1]+Image[ligne,colonne]+Image[ligne,colonne+1]
            if somme>=1 :
                    resultat[ligne,colonne]=1
               
    return resultat

def ouvertureDisque(Image):
    resultat=dilatationDisque(erosionDisque(Image))
    return resultat

def fermetureDisque(Image):
    resultat=erosionDisque(dilatationDisque(Image))
    return resultat

def epaiciSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and Image[ligne-1,colonne]==1:
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==0) and Image[ligne+1,colonne]==0:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if  Image[ligne,colonne]==1 :
                        resultat[ligne,colonne]=1
               
    return resultat


def aminciUnSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) :
                #ligne du bas
                if Image[ligne+1,colonne]==0:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1  and Image[ligne,colonne+1]==0:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciDeuxSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne]==0) :
                #ligne du bas
                if Image[ligne+1,colonne-1]==1:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1  and Image[ligne,colonne+1]==0:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciTroisSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==0) and Image[ligne-1,colonne]==0:
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==1) and Image[ligne+1,colonne]==1:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if  Image[ligne,colonne]==1 :
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciQuatreSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==0) :
                #ligne du bas
                if Image[ligne+1,colonne]==1:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if Image[ligne,colonne-1]==0 and Image[ligne,colonne]==1  and Image[ligne,colonne+1]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def aminciCinqSi(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne]==1) :
                #ligne du bas
                if Image[ligne+1,colonne-1]==0:
                    #ligne actuelle Image[ligne,colonne-1]==0 and and Image[ligne,colonne+1]==1
                    if Image[ligne,colonne-1]==0 and Image[ligne,colonne]==1  and Image[ligne,colonne+1]==1:
                        resultat[ligne,colonne]=0
               
    return resultat

def tourCompletSi(Image):
    
    resultat=aminciCinqSi(aminciQuatreSi(aminciTroisSi(aminciDeuxSi(aminciUnSi(aminciSi(Image))))))
    
    return resultat

def homothopiqueSi(Image,nombreIte):
    resultat = tourCompletSi(Image)
    resultatSuivant=tourCompletSi(resultat)
    
    """while (resultatSuivant == resultat).all() :
        #tampon=resultatSuivant
        resultat=resultatSuivant
        resultatSuivant=tourCompletAminci(resultat)"""
    for i in range(nombreIte):
        resultat=tourCompletSi(resultatSuivant)
        resultatSuivant=resultat
    
    return resultat