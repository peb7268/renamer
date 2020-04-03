'''
#NOTES ************************************************
type(): is python's equivilent to typeof

#TODOS:

* Loop over the directory listing:
- If its a file, I want to put it in a directory
- If its a directory, I want to validate the name

# Directory naming rules
- Take Filename and replace . with spaces
- remove .mp4, .avi, and .mpk suffixes

# Filename naming rules
- just copy them into the folder
'''

import os
import pprint

#Configure printer
pp = pprint.PrettyPrinter(indent=4)


def insertFileIntoDir(fileName):
    print("fomratting fileName" + fileName)
    #Make dirname according to rules
    #move file into dir

def formatDirectoryName(dirName):
    print("fomratting dirName" + dirName)

basePath    = '/volume1/homes/media/plex/Movies'
entries     = os.listdir(basePath)
for entry in entries:
    # line = type(entry).__name__ + " :" + entry
    # pp.pprint(entry)
    if os.path.isfile(os.path.join(basePath, entry)):
        insertFileIntoDir(entry)
    elif os.path.isdir(os.path.join(basePath, entry)):
        formatDirectoryName(entry)