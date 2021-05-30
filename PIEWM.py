#! /usr/bin/env python3

#PIEWM : PyInstaller .Exe/Windows Maker

#imports
import sh
from alive_progress import alive_bar

pypath = input("Please enter the path to the .py file. Do not enter the file name, just the folder it lives in: ")
pyfile = input("What is the file name? (Just the .py file): ")
if ".py" not in pyfile:
    pyfile = pyfile + ".py"
onefile = input("Would you like to use the one-file flag? (Y/N): ")

sh.cd(pypath)

with alive_bar(1, title = "Working...", spinner = 'classic', length = 3) as bar:
    if onefile.lower() == "y" or "yes" or "true":
        sh.wine("cmd", "/c", "pyinstaller", "-F", pyfile)
        bar()
        print("Completed!")
    elif onefile.lower() == "n" or "no" or "false":
        sh.wine("cmd", "/c", "pyinstaller", pyfile)
        bar()
        print("Completed!")
    else:
        bar()
        print("Sorry, invalid option (One-File Flag Boolean)")