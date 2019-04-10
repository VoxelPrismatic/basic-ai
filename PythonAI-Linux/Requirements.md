# Requirements
## All versions of this code is run on Linux, but also can be run on all OSs with minor modification

### Version 6, 6a, 6b
Modifications:
     
     Windows: `py -3.7` instead of `python3.7`
     
     Debian Linux: `python3.7` (Ubuntu and more)
     
     Mac: `python3.7` or just use the PythonLauncher [here](https://www.python.org/downloads/release/python-371/)

#### Dependencies
Python Version: `3.7.1`

     Linux `sudo apt install python3.7`
     
     Mac [here](https://www.python.org/downloads/release/python-371/) (makes life easy)
     
     Windows [here](https://medium.com/@itylergarrett.tag/how-to-install-python-3-7-on-windows-10-pc-the-non-developer-version-b063e1913b39) 
     
Discord.py Version: `1.0.0a`
     
     Linux `python3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite`
     
     Windows `py -3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite`
     
     Mac `python3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite`
     
Discord Voice (for the future): 
     
     Linux `python3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite[voice]`
     
     Windows `py -3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite[voice]`
     
     Mac `python3.7 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite[voice]`

Pip (idk) - `apt install python3-pip`

AIO Files Version 0.4.0:
     
     Linux `python3.7 -m pip install aiofiles`
     
     Windows `py -3.7 -m pip install aiofiles`
     
     Mac `python3.7 -m pip install aiofiles`
     
#### Files
Once you have chosen a folder to keep the program in, be sure to do the above imports again in the folder, in case.

Then proceed to make the following text files, yes the names are important:
     
`PrismaticText` // `PrismaticM2M-R` // `PrismaticM2M-C` // `MathIn` // `MathOut` // `SciIn` // `SciOut` // `EngIn` // `EngOut`

Those text files represent seperate arrays, making it easy to see which stuff it learned

Once created, add your responses to `PrismaticText`, where each line represents a new response. If you want a multi-line response, use `\n`

### Version 3

Same as above, but all `3.7` should be replaced with `3` because it uses Python `3.6.x` rather than `3.7.x`

**Do not attempt to run version 6 with Python 3.6.x, it will fail**, however you can run version 3 with python3.7.x with no issues :D
