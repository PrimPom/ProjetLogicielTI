# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:07:06 2019

@author: primp
"""
from aminciHuConnexite import aminciHuConnexite
from aminciLun import aminciLun
from aminciLdeux import aminciLdeux
from aminciLtrois import aminciLtrois
from aminciLquatre import aminciLquatre
from aminciLcinq import aminciLcinq
from aminciLsix import aminciLsix
from aminciLsept import aminciLsept

def tourCompletAminci(Image):
    
    resultat = aminciLsept(aminciLsix(aminciLcinq(aminciLquatre(aminciLtrois(aminciLdeux(aminciLun(aminciHuConnexite(Image))))))))
   
               
    return resultat