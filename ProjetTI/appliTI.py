# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:37:34 2019

@author: primp
"""

from numpy import arange, sin, pi

import matplotlib

# uncomment the following to use wx rather than wxagg
matplotlib.use('WX')
#from matplotlib.backends.backend_wx import FigureCanvasWx as FigureCanvas

# comment out the following to use wx rather than wxagg
#matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

from matplotlib.backends.backend_wx import NavigationToolbar2Wx

from matplotlib.figure import Figure

import wx.lib.mixins.inspection as WIT


import wx
from seuillageImage import seuillageImage
from niveauDegris import imageEnNiveauDeGris

APP_ERASE=0
APP_EXIT = 1
APP_SEUILLAGE=2
APP_ADDITION=3
APP_SOUSTRACTION=4
APP_EROSION_Carre=5
APP_EROSION_Cercle=6
APP_DILATATION_Carre=7
APP_OUVRIR_Carre=8
APP_OUVRIR_Cercle=9
APP_FERMER_Carre=10
APP_FERMER_Cercle=11
APP_AMINCIR_Carre=12
APP_AMINCIR_Cercle=13
APP_EPAISSIR_Carre=14
APP_EPAISSIR_Cercle=17
APP_HOMO_Carre=15
APP_LANTUEJOUL_Carre=16
APP_DILATATION_Cercle=18

global newfile
"""from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np"""

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
from comparateur import comparateurDeTailleDimage
from aminciHuConnexite import aminciHuConnexite,aminciLun,aminciLdeux,aminciLtrois,aminciLquatre,aminciLcinq,aminciLsix,aminciLsept,tourCompletAminci,homothopique
from lantuejoulHuConnexite import lantuejoulHuConnexite
from aminciHuConnexite import aminciHuConnexite
from epaiciHuConnexite import epaiciHuConnexite
from tourCompletAminci import tourCompletAminci 
from imageHexagonale import imageHexagonale
from aminciSiConnexite import aminciSi,aminciUnSi,tourCompletSi,homothopiqueSi,epaiciSi,erosionDisque,dilatationDisque,ouvertureDisque,fermetureDisque
#from homothopique import homothopique

from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np




class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()     
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("gray")
        
        #PREMIER menu bar
        fileMenu = wx.Menu()
        #fileMenu.Append(wx.ID_NEW, '&New')
        #fileMenu.Append(wx.ID_OPEN, '&Charger une image')
        #fileMenu.Append(wx.ID_SAVE, '&Enregistrer')
        
        qmiLoad = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Charger une novelle image')
        qmiLoad.SetBitmap(wx.Bitmap('images/picture.png'))
        fileMenu.Append(qmiLoad)
        
        qmiErase = wx.MenuItem(fileMenu, APP_ERASE, '&Effacer l\'imager')
        qmiErase.SetBitmap(wx.Bitmap('images/erase.png'))
        fileMenu.Append(qmiErase)
        
        
        qmiSave = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Enregistrer\tCtrl+S')
        qmiSave.SetBitmap(wx.Bitmap('images/diskette.png'))
        fileMenu.Append(qmiSave)
        
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quitter\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('images/logout.png'))
        fileMenu.Append(qmi)
        
        self.Bind(wx.EVT_MENU, self.OnErase, id=APP_ERASE)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)

        menubar.Append(fileMenu, '&Fichier')
        
        
          #Deuxieme menu bar
        fileMenu2 = wx.Menu()
        fileMenu2.Append(APP_SEUILLAGE, '&Seuillage d\'une image')
        fileMenu2.Append(APP_ADDITION, '&Addition de deux images')
        fileMenu2.Append(APP_SOUSTRACTION, '&Soustraction de deux images')
        fileMenu2.AppendSeparator()
        
        eros = wx.Menu()
        eros.Append(APP_EROSION_Cercle, 'Structurant Disque')
        eros.Append(APP_EROSION_Carre, 'Structurant Carré')
        fileMenu2.AppendMenu(wx.ID_ANY, '&Erosion d\'image ', eros)
        
        dilat = wx.Menu()
        dilat.Append(APP_DILATATION_Cercle, 'Structurant Disque')
        dilat.Append(APP_DILATATION_Carre, 'Structurant Carré')
        

        fileMenu2.AppendMenu(wx.ID_ANY, '&Dilatation d\'image ', dilat)
        
        self.Bind(wx.EVT_MENU, self.OnSeuillage, id=APP_SEUILLAGE)
        self.Bind(wx.EVT_MENU, self.OnAddition, id=APP_ADDITION)
        self.Bind(wx.EVT_MENU, self.OnErosionCarre, id=APP_EROSION_Carre)
        self.Bind(wx.EVT_MENU, self.OnErosionDisque, id=APP_EROSION_Cercle)
        self.Bind(wx.EVT_MENU, self.OnDilatationCarre, id=APP_DILATATION_Carre)
        self.Bind(wx.EVT_MENU, self.OnDilatationCercle, id=APP_DILATATION_Cercle)
        menubar.Append(fileMenu2, '&Opérations Simples')
        
        
              #Troisieme menu bar
        fileMenu3 = wx.Menu()
            
        ouvert = wx.Menu()
        ouvert.Append(APP_OUVRIR_Cercle, 'Structurant Disque ')
        ouvert.Append(APP_OUVRIR_Carre, 'Structurant Carré')
        fileMenu3.AppendMenu(wx.ID_ANY, '&Ouverture d\'une image ', ouvert)
        
        ferme = wx.Menu()
        ferme.Append(APP_FERMER_Cercle, 'Structurant Disque*')
        ferme.Append(APP_FERMER_Carre, 'Structurant Carré')
        fileMenu3.AppendMenu(wx.ID_ANY, '&Fermeture d\'une image ', ouvert)
        fileMenu3.AppendSeparator()
        aminci = wx.Menu()
        aminci.Append(APP_AMINCIR_Cercle, 'Structurant Disque')
        aminci.Append(APP_AMINCIR_Carre, 'Structurant Carré')
        fileMenu3.Append(wx.ID_ANY, '&Amincissement',aminci)
        epaici = wx.Menu()
        epaici.Append(APP_EPAISSIR_Cercle, 'Structurant Disque')
        epaici.Append(APP_EPAISSIR_Carre, 'Structurant Carré')
        fileMenu3.Append(wx.ID_ANY, '&Epaississement',epaici)
         
        self.Bind(wx.EVT_MENU, self.OnOuvrirCarre, id=APP_OUVRIR_Carre)
        self.Bind(wx.EVT_MENU, self.OnOuvrirCercle, id=APP_OUVRIR_Cercle)
        self.Bind(wx.EVT_MENU, self.OnFermerCarre, id=APP_FERMER_Carre)
        self.Bind(wx.EVT_MENU, self.OnFermerCercle, id=APP_FERMER_Cercle)
        self.Bind(wx.EVT_MENU, self.OnAmincirCercle, id=APP_AMINCIR_Cercle)
        self.Bind(wx.EVT_MENU, self.OnAmincirCarre, id=APP_AMINCIR_Carre)
        self.Bind(wx.EVT_MENU, self.OnEpaissirCarre, id=APP_EPAISSIR_Carre)
        self.Bind(wx.EVT_MENU, self.OnEpaissirCercle, id=APP_EPAISSIR_Cercle)
        menubar.Append(fileMenu3, '&Opérations Complexes')
        
        #Quatrieme menu bar
        fileMenu4 = wx.Menu()
        fileMenu4.Append(APP_LANTUEJOUL_Carre, '&Squellette par Lantuejoul')
        fileMenu4.Append(APP_HOMO_Carre, '&Squellette par amincissement homotopique')   
        
        self.Bind(wx.EVT_MENU, self.OnAminciHomothopiqueCarre, id=APP_HOMO_Carre)
        self.Bind(wx.EVT_MENU, self.OnLantuejoulCarre, id=APP_LANTUEJOUL_Carre)
        menubar.Append(fileMenu4, '&Opérations Avancées')

        self.SetMenuBar(menubar)     
        self.SetSize((1000, 600))
        self.SetTitle('AppliTI')
        self.Centre()
        
    def OnErase(self,e):
        self.panel.SetBackgroundColour("gray")
        print("ERAAAAAAAAAAAAAAAAAAASSSSSSSSSSSSSSSSEEEE")
        
    def OnQuit(self, e):
        self.Close()
        
    def OnOpen(self, event):
        
        # Create open file dialog
        openFileDialog = wx.FileDialog(self, "Open", "", "", 
                                       "PNG files (*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        global newfile
        newfile=openFileDialog.GetPath()
        global image,imageTableau,imageSeuille
        
        image=Image.open(newfile)
        
        #Transformation de l'image en tableau
        imageTableau = np.asarray(image)
        imageSeuille=seuillageImage(imageEnNiveauDeGris(imageTableau),0.5)
        print(openFileDialog.GetPath())
              
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap(openFileDialog.GetPath(), wx.BITMAP_TYPE_ANY))
        openFileDialog.Destroy()
        self.mincol.SetPosition((40, 160))        
        """imgORIG = wx.Image(newfile, wx.BITMAP_TYPE_ANY)
        global  resultat
        resultat = imgORIG.ConvertToBitmap()"""
        
    def OnErosionCarre(self, e):
        imageErode=erosionImage(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Erosion 8-connexité")
        plt.imshow(imageErode,cmap='gray')
        
    def OnErosionDisque(self,e):
        imageErode=erosionDisque(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Erosion 6-connexité")
        plt.imshow(imageErode,cmap='gray')
        
        
    def OnEpaissirCercle(self,e):
        imageEpaici=epaiciSi(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Epaicissement en 6-connexité")
        plt.imshow(imageEpaici,cmap='gray')
        
    def OnLantuejoulCarre(self,e):
        imageLantue=lantuejoulHuConnexite(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Lantuejoule en 8-Connexité")
        plt.imshow(imageLantue,cmap='gray')
        
    def OnAmincirCercle(self,e):
        imageAminci=aminciSi(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Amincissement en 6-connexité")
        plt.imshow(imageAminci,cmap='gray')
        
    def OnOuvrirCarre(self,e):
        imageOuvert=ouvertureImage(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Ouverture 8-connexité")
        plt.imshow(imageOuvert,cmap='gray')
    
    def OnOuvrirCercle(self,e):
        imageOuvert=ouvertureDisque(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Ouverture 6-connexité")
        plt.imshow(imageOuvert,cmap='gray')
    
    def OnFermerCarre(self,e):
        imageFermee=fermetureImage(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Fermeture 8-connexité")
        plt.imshow(imageFermee,cmap='gray')
        
    def OnFermerCercle(self,e):
        imageFermee=fermetureDisque(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Fermeture 6-connexité")
        plt.imshow(imageFermee,cmap='gray')
       
        
    def OnDilatationCarre(self,e):
        imageDilate=dilatationImage(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Dilatation 8-connexité")
        plt.imshow(imageDilate,cmap='gray')
        
    def OnDilatationCercle(self,e):
        imageDilate=dilatationDisque(imageHexagonale(imageSeuille))
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Dilatation 6-connexité")
        plt.imshow(imageDilate,cmap='gray')
        
    def OnAmincirCarre(self,e):
        imageAmincie=aminciHuConnexite(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Amincissement 8-connexité")
        plt.imshow(imageAmincie,cmap='gray')
    
    def OnEpaissirCarre(self,e):
        imageEpaissie=epaiciHuConnexite(imageSeuille)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Epaicissement 8-Connexité")
        plt.imshow(imageEpaissie,cmap='gray')
        
    def OnAminciHomothopiqueCarre(self,e):
        squelette=homothopique(imageSeuille,25)
        #print("ICCCCCCCCCCCCCCCCCCCCCIIIIIIIIIIIIIIIIIIII")
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)       
        #Ca fait sortir une fenetre figure       
        plt.figure(figsize=(8,8))
        plt.title("Amincissement homothopique 8-connexité")
        plt.imshow(squelette,cmap='gray')
        
    def OnSeuillage(self, e):
        imageSeuille=seuillageImage(imageEnNiveauDeGris(imageTableau),0.5)     
        img=Image.fromarray(imageSeuille)      
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.title("Seuillage")
        plt.imshow(imageSeuille,cmap='gray')
        
        """
        mpimg.imsave("imageSeuille.png", imageEnNiveauDeGris(imageSeuille))
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap('imageSeuille.png', wx.BITMAP_TYPE_ANY))
        
        self.mincol.SetPosition((160, 160))"""
        
    def OnAddition(self, e):
        imageSeuille=seuillageImage(imageTableau,0.5)        
        #Transformation de l'image en tableau
        imageAadditionner = self.ouvertureDialog()    
        
        imageSeuille2=seuillageImage(imageAadditionner,160)
        
        if comparateurDeTailleDimage(imageSeuille,imageSeuille2)==1:
            addition=additionImage(imageSeuille,imageSeuille2)
        
            self.figure = Figure()
            self.axes = self.figure.add_subplot(111)     
            #Ca fait sortir une fenetre figure
            plt.figure(figsize=(8,8))
            plt.imshow(addition,cmap='gray')
        else:
            self.showMessage(self)
         
     
   
        
    def showMessage(self):
        wx.MessageBox('Les deux images n\'ont pas la même taille ','Erreur Addition',
            wx.OK | wx.ICON_ERROR)       

        
    def ouvertureDialog(self):
        #Creation d'une boite de selection pour l'image
        openFileDialog = wx.FileDialog(self, "Open", "", "", 
                                       "PNG files (*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()       
        fichierAadditionner=openFileDialog.GetPath()      
        image=Image.open(fichierAadditionner)     
        #Transformation de l'image en tableau
        imageArray = np.asarray(image)
        openFileDialog.Destroy()
        
        return imageArray

       




def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()