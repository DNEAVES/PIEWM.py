# PIEWM.py

## PyInstaller .Exe/Windows Maker

A simple script to make Windows .exe files from python scripts on Linux/Unix.

I used these commands frequently when packaging the Python Twitchbot for my friend, so I made it even easier for myself to convert .py files to .exe by packing it all into one python script to do the conversion.

Why an .exe file? It's easier for people who dont have python interpreters and modules installed to run one executable.

### Requires Python 3.x, [sh](https://github.com/amoffat/sh) and [alive-progress](https://github.com/rsalmei/alive-progress) from pip, and [wine](https://wiki.winehq.org/Download)

## How to use it?

I recommend aliasing the command in `.bashrc`, `.zshrc`, etc. Be sure to source commands.

Then just run the script. It will prompt for the information it needs (directory to work from, file to use).
It also supports relative directories, so if you're already working within the directory the files live in, you can enter `./` as the directory prompt.
It will take a few seconds but when it's done your .exe file will be in `./dist/`

Note: I use the `--onefile` flag by choice, as it's easier for me to send one .exe file to my friend.
Feel free to learn the code and adjust it to your needs (as long as you comply with the MIT license stuff).
