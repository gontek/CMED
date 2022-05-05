# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:43 2022
save to a C drive location to make it faster and avoid the "already exists repladce yes/no question on each download"
The weekly download list contains mostly reports we already have that need to be overwritten for some reason

This is python 3 code written and run in Spyder 

in chrome:
    settings, advanced, set download directory
    make it so they dont auto open in bluebeam
    
Sleep (time in seconds) is how long you will have to download the pdf when it opens, 12 seconds is about the fastest rate I can handle with great performacnce
30 seconds gives ample time to download given non perfect internet/network performance and allows time to briefly review each crash report
consider also hte number of records in the file to download which has ranged from 65-185

copy downloaded files to \\citydata\public\MSO_Engr\KDOT\CrashReports

log into TRS at https://portal.kstrs.org/private/SimpleSearch.aspx

@author: kgonterwitz
"""

import webbrowser
#import pdfkit
from time import sleep

sleeptime = 24

ws = r'//citydata/public/MSO_Engr/KDOT/CrashReports/'
download_folder = r'C:/Users/kgonterwitz'



text_file = ws+"KDOT2022042601.txt"
#text_file = ws+"KDOTtest.txt"
from numpy import loadtxt
lines = loadtxt(text_file, dtype=str, comments="#", delimiter=" | ", unpack=False)

for line in lines:
    
    file_name = str((line[0:1]))[2:13]+".pdf"
    print(file_name)
    url = "https://portal.kstrs.org/private/PDF.aspx?itemID="+str((line[1:2]))[2:10]+"&VerNbr=1&rType=PDF&rSource=AccidentLib"
    print(url)
    webbrowser.open(url, new=0, autoraise=True)
    #pdfkit.from_url(url, file_name)
    sleep(sleeptime)
