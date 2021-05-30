# PIEWM.py

##PyInstaller .Exe/Windows Maker

A simple script to make Windows .exe files from python scripts on Linux/Unix.

I used these commands frequently when packaging the Python Twitchbot for my friend, so I made it even easier for myself to convert .py files to .exe by packing it all into one python script to do the conversion.
Why an .exe file? It's easier for people who dont have python interpreters and modules installed to run one executable.

###Requires [sh](https://github.com/amoffat/sh) and [alive-progress](https://github.com/rsalmei/alive-progress) from pip, and [wine](https://wiki.winehq.org/Download)

##How to use it?

I recommend aliasing the command or copying it to a `/bin/` directory that makes sense for you (Whether its `/bin/`, `/usr/bin`, `/usr/local/bin/`, whatever it may be). Be sure to update/source commands if you do this.

Then just run the script. It will prompt for the information it needs (directory to work from, file to use).
It also supports relative directories, so if youre already working within the directory the files live in, you can do `./` as the directory prompt.
It will take a few seconds but when its done your .exe will be in `./dist/`

Note: I use the `--onefile` flag by choice, as it's easier for me to send one .exe file to my friend.
Feel free to learn the code and adjust it to your needs (as long as you comply with the MIT license stuff).
