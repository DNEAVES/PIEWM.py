#! /usr/bin/env python3

#PIEWM : PyInstaller .Exe/Windows Maker

#Imports
import sh
from alive_progress import alive_bar

#Get File/Folder info
pypath = input("Please enter the path to the .py file. Do not enter the file name, just the folder it lives in: ")
pyfile = input("What is the file name? (Just the .py file): ")
#Forgot the ".py"? We got you!
if ".py" not in pyfile:
    pyfile = pyfile + ".py"
    
#Move to directory
sh.cd(pypath)

#Show progress bar while doing the work
with alive_bar(1, title = "Working...", spinner = 'classic', length = 3) as bar:
    sh.wine("cmd", "/c", "pyinstaller", "-F", pyfile)
    bar()
    print("Completed!")
