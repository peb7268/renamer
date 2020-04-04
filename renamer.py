#!/usr/bin/env python
#chmod +x renamer.py

'''
#NOTES ************************************************

pdb: python debugger
type(): is python's equivilent to typeof
s(tep)
Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).

n(ext)
Continue execution until the next line in the current function is reached or it returns. (The difference between next and step is that step stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

unt(il)
Continue execution until the line with the line number greater than the current one is reached or when returning from current frame.

New in version 2.6.

r(eturn)
Continue execution until the current function returns.

c(ont(inue))
Continue execution, only stop when a breakpoint is encountered.

j(ump) lineno
Set the next line that will be executed. Only available in the bottom-most frame. This lets you jump back and execute code again, or jump forward to skip code that you don’t want to run.

It should be noted that not all jumps are allowed — for instance it is not possible to jump into the middle of a for loop or out of a finally clause.

l(ist) [first[, last]]
List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing. With one argument, list 11 lines around at that line. With two arguments, list the given range; if the second argument is less than the first, it is interpreted as a count.

a(rgs)
Print the argument list of the current function.

q(uit)
Quit from the debugger. The program being executed is aborted.

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

import os, sys, getopt

import pprint
import pdb

#Configure printer
pp = pprint.PrettyPrinter(indent=4)

basePath = ""
argv     = sys.argv[1:]

try:
    print("grabbing args from cli")
    opts, args = getopt.getopt(argv,"p:",["path="])
except getopt.GetoptError:
      print('cli err renamer.py -p </path/to/files>')
      sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('renamer.py -p </path/to/files>')
        sys.exit()
    elif opt in ("-p", "--path"):
        basePath = arg

def insertFileIntoDir(basePath, fileName):
    print("fomratting fileName " + fileName)
    filename    = sanitizeFileName(fileName)
    dirname     = resolveDirnameFromFile(basePath, filename)

    '''
    if filename exists in dir
    then alias the file to the same directory but underscore it
    create the directory
    then move the file into the directory and remove the underscore
    '''
    
    if not os.path.exists(dirname):
        #Make dirname according to rules
        os.mkdir(dirname)
        here    = basePath + "/" + fileName
        there   = dirname + "/" + filename
        os.rename(here, there)
        pp.pprint("moving file from " + here + " to  " + there)
    else:
        print("dir " + filename + " already exists, aliasing dirname")
        pdb.set_trace()

        fileAlias = basePath + "/_" + filename
        os.rename(basePath + "/" + filename, fileAlias)
        os.mkdir(dirname)
        os.rename(fileAlias, dirname + "/" + filename)
    
def sanitizeFileName(filename):
    _filename   = filename
    _filename   = _filename.replace("[", "")
    _filename   = _filename.replace("]", "")
    _filename   = _filename.replace("-", ".")
    return _filename

def resolveDirnameFromFile(basePath, filename):
    _dirname = filename
    _dirname   = _dirname.replace(".mp4", "")
    _dirname   = _dirname.replace(".avi", "")
    _dirname   = _dirname.replace(".mkv", "")
    return basePath + "/" + _dirname

def formatDirectory(dirName):
    print("formatting directory")
    formatDirectoryName(dirName)
    formatDirectoryContents(dirName)

def formatDirectoryContents(dirName):
    print("fomratting dirName " + dirName)
    pdb.set_trace()
    
def formatDirectoryName(dirName):
    print("fomratting dirName " + dirName)


entries     = os.listdir(basePath)
for entry in entries:
    # line = type(entry).__name__ + " :" + entry
    # pp.pprint(entry)
    if os.path.isfile(os.path.join(basePath, entry)):
        insertFileIntoDir(basePath, entry)
    elif os.path.isdir(os.path.join(basePath, entry)):
        formatDirectory(entry)