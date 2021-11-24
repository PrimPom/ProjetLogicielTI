# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:11:16 2019

@author: primp
"""
from erosionImage import erosionImage
from dilatationImage import dilatationImage

def ouvertureImage(Image):
    
    return  dilatationImage(erosionImage(Image))