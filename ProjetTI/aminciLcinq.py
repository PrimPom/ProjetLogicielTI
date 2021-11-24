# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:00:24 2019

@author: primp
"""

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