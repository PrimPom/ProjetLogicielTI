# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:30:28 2019

@author: primp
"""

#Importation des différentes fonctions du projet 
from binarisation import binarisation
from histogramm import histogramme
from niveauDegris import imageEnNiveauDeGris
from seuillageImage import seuillageImage
from additionImage import additionImage
from soustractionImage import soustractionImage
from erosionImage import erosionImage
from dilatationImage import dilatationImage
from ouvertureImage import ouvertureImage
from fermetureImage import fermetureImage
from aminciHuConnexite import aminciHuConnexite,aminciLun,aminciLdeux,aminciLtrois,aminciLquatre,aminciLcinq,aminciLsix,aminciLsept,tourCompletAminci,homothopique
from epaiciHuConnexite import epaiciHuConnexite
#from tourCompletAminci import tourCompletAminci 
#from homothopique import homothopique
from imageHexagonale import imageHexagonale
from aminciSiConnexite import aminciSi,aminciUnSi,tourCompletSi,homothopiqueSi,erosionDisque,dilatationDisque,ouvertureDisque,fermetureDisque
from lantuejoulHuConnexite import lantuejoulHuConnexite
##########################
"""
from aminciLun import aminciLun
from aminciLdeux import aminciLdeux
from aminciLtrois import aminciLtrois
from aminciLquatre import aminciLquatre
from aminciLcinq import aminciLcinq
from aminciLsix import aminciLsix
from aminciLsept import aminciLsept
from tourCompletAminci import tourCompletAminci

####################"""""

from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2 
import numpy as np 
  

#Lecture image couleur Granule1.bmp:Peppers.png 0,4 images.png ,dtype=np.dtype('d')
im_in_granule = Image.open("Peppers.png")
#Transformation de l'image en tableau
im_color_granule = np.asarray(im_in_granule)
#print(im_color_granule)

#imageGrise=imageEnNiveauDeGris(im_color_granule)
imageSeuille1=seuillageImage(imageEnNiveauDeGris(im_color_granule),0.4)
imageSeuille2=seuillageImage(imageEnNiveauDeGris(im_color_granule),167)
aAfficher=tourCompletAminci(imageSeuille1)

#print(imageEnNiveauDeGris(im_color_granule)) lantuejoulHuConnexite(imageSeuille1)

#Affichage image:
plt.figure(figsize=(10,10))
plt.imshow(imageSeuille1,cmap='gray')

plt.figure(figsize=(10,10))
plt.imshow(fermetureDisque(imageHexagonale(imageSeuille1)),cmap='gray')

plt.figure(figsize=(10,10))
plt.imshow(homothopique(imageSeuille1,25),cmap='gray')

#plt.imshow(cv2.erode(imageSeuille1,kernel,5))
#tourCompletAminci(tourCompletAminci(tourCompletAminci(tourCompletAminci(aAfficher)))))


#(resultatSuivant == resultat).all ==False 
#if np.array_equal( np.asarray(dilatationImage(imageSeuille1)),erosionImage(imageSeuille1)):
if(homothopique(imageSeuille1,1)==aAfficher).all():
    print("Egaux::::::")