# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:20:34 2019

@author: primp
"""
from tourCompletAminci import tourCompletAminci
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