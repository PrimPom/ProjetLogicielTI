# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:47:34 2019

@author: primp
"""

     
def comparateurDeTailleDimage(image1,image2):
        retour=False;
        if (image1.shape==image2.shape).all():
            retour=1
        
        return retour