# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:43 2022
20220104700
20110006152

@author: kgonterwitz
"""

import webbrowser
from time import sleep

ws = r'//citydata/public/MSO_Engr/KDOT/CrashReports/'
download_folder = r'C:/Users/kgonterwitz'



text_file = ws+"KDOT2022040402.txt"
text_file = ws+"KDOTtest.txt"
from numpy import loadtxt
lines = loadtxt(text_file, dtype=str, comments="#", delimiter=" | ", unpack=False)

for line in lines:
    
    file_name = str((line[0:1]))[2:13]+".pdf"
    print(file_name)
    url = "https://portal.kstrs.org/private/PDF.aspx?itemID="+str((line[1:2]))[2:10]+"&VerNbr=1&rType=PDF&rSource=AccidentLib"
    print(url)
    webbrowser.open(url, new=0, autoraise=True)
    sleep(10)


    sleep(2) 