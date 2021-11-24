# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:14:19 2019

@author: primp
"""

from erosionImage import erosionImage
from dilatationImage import dilatationImage

def fermetureImage(Image):
    
    return  erosionImage(dilatationImage(Image))