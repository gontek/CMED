'''
Created on Jan 19, 2023

compare pdf files in crash reports to crash report IDs in text files

@author: kgonterwitz
'''
#import cv2
#import pytesseract
import os
from numpy import loadtxt

path = r"\\citydata\public\MSO_Engr\KDOT\CrashReports"

# to store files in a list
textlist = []
pdflist = []
print(path)
print("Text files:")
# dirs=directories
for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
            print(f)
            lines = loadtxt(path+r"/"+f, dtype=str, comments="#", delimiter=" | ", unpack=False)
            for line in lines:
                txtcrashkey = str((line[0:1]))[2:13]
                if txtcrashkey not in textlist:
                #this if make the list unique
                #print(txtcrashkey)
                    textlist.append(txtcrashkey)
 
for (root, dirs, file) in os.walk(path):
    for p in file:
        if '.pdf' in p:
            pdfcrashkey = p[0:11]
            #print(pdfcrashkey)
            pdflist.append(pdfcrashkey)

crashkeynotlisted = []
textlist.remove("ACCIDENT_KE")
textlist.sort(reverse=True)
pdflist.sort(reverse=True)


print("pdfs missing include:")
for crashkey in textlist:
    if crashkey not in pdflist:
            print(crashkey)
            crashkeynotlisted.append(crashkey)
            
            
    