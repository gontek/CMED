'''
Created on Oct 7, 2022

for now this script is designed to take a list of assets that Trekk has panoramic photos of and process that list into ArcGIS for popups that link to the image viewer

the url index directory at https://trekk360.com/viewers/Lawrence_Storm/Pano/ contains the list of structures with images

the format of the directories within that site are "Asset ID" underscore "date of photo"

what is needed is to retrieve the listed directories, split the asset ID for joining to the feature in GIS, and provide link to url for the viewer in the format of 

https://trekk360.com/viewers/Lawrence_Storm/Pano/10001_20220527/output/viewer.html

where 10001 is the asset ID and the date portion is the most recent date of the pano images - there can be multiple dates for each asset.

@author: kgonterwitz
'''
'''
python trouble shoot after pro3 update

delete old cloned environments 
if possible update path and pythonpath system variables
clone python using conda not arcgis pro environment manager if you are not admin, clone in same directory as pro would put it in

https://developers.arcgis.com/python/guide/understanding-conda/

use conda to install packages not pro environment manager if you are not admin

use conda to fix version of numpy, the default distribution is an incompatible version.  


print('python basically works')
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))
import numpy
from numpy import loadtxt

'''

trekklist = r'\\citydata\users\kgonterwitz\TrekkList20221007.txt'

import numpy

lines = numpy.loadtxt(trekklist, dtype=str, comments="#", delimiter=",", unpack=False)
index = 0

for line in lines:
    index +=1
    link_name = str((line[0:1]))[2:16]
    asset = link_name.split('_')[0]
    print(str(link_name),',', str(asset))