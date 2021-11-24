# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:51:01 2019

@author: primp
"""

# otherwise ask the user what new file to open
         """with wx.FileDialog(self, "Charger un fichier", wildcard="PNG files (*.png)|*.png",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     # the user changed their mind
                pathname = wx.FileDialog.GetPath()
                 
                print(pathname)
                try:
                    with open(pathname, 'r') as file:
                        self.doLoadDataOrWhatever(file)
                except IOError:
                    wx.LogError("Cannot open file '%s'." % newfile)"""