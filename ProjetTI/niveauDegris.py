# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:03:18 2019

@author: primp
"""
from skimage.color import rgb2gray
# transformation image couleur en niveaux de gris:
def imageEnNiveauDeGris(image):
    niveauDeGris=rgb2gray(image)

    return niveauDeGris