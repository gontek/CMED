# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 09:09:43 2022
save to a C drive location to make it faster and avoid the "already exists repladce yes/no question on each download"
The weekly download list contains mostly reports we already have that need to be overwritten for some reason

This is python 3 code written and run in Spyder 

in chrome:
    settings, advanced, set download directory
    make it so they dont auto open in bluebeam
    highlight red text with file name
    control+c
    click pdf download button
    control+v
    save
    
Sleep (time in seconds) is how long you will have to download the pdf when it opens, 12 seconds is about the fastest rate I can handle
16-20 seconds gives ample time to download given non perfect internet/network performance and allows time to briefly review each crash report
consider also hte number of records in the file to download which has ranged from 65-185

you can also add a breakpoint in the for loop and step through each one individually in debug mode, setting sleep time to 1 or 0

some files reference 2011 or older crashes that cant be queried in the TRS

copy downloaded files to \\citydata\public\MSO_Engr\KDOT\CrashReports

log into TRS at https://portal.kstrs.org/private/SimpleSearch.aspx

@author: kgonterwitz
"""

import webbrowser
#import pdfkit
from time import sleep

sleeptime = 18

ws = r'//citydata/public/MSO_Engr/KDOT/CrashReports/'
#move the list local while hte VPN is down
ws = r'C:/Users/kgonterwitz/Downloads/crashdownload20220726/'
download_folder = r'C:/Users/kgonterwitz/Downloads/crashdownload20220726'

#start a counter to print and match to text file line numbers
#open list in notepad ++ and turn on row numbers
#if a file isnt downloaded in time it can be quickly retrieved from the TRS url
index = 0


text_file = ws+"KDOT20220801.txt"
#text_file = ws+"KDOTtest.txt"
from numpy import loadtxt
lines = loadtxt(text_file, dtype=str, comments="#", delimiter=" | ", unpack=False)

for line in lines:
    index +=1
    file_name = str((line[0:1]))[2:13]+".pdf"
    print(str(index)+" "+str(file_name))
    url = "https://portal.kstrs.org/private/PDF.aspx?itemID="+str((line[1:2]))[2:10]+"&VerNbr=1&rType=PDF&rSource=AccidentLib"
    webbrowser.open(url, new=0, autoraise=True)
    sleep(sleeptime)
