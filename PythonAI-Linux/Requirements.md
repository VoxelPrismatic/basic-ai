# Requirements
## All versions of this code is run on Linux, but also can be run on all OSs with minor modification

### Latest
Modifications:

     Windows: `py -3.7` instead of `python3.7`

     Debian Linux: `python3.7` (Ubuntu and more)

     Mac: `python3.7` or just use the PythonLauncher [here](https://www.python.org/downloads/release/python-371/)

#### Dependencies
Python: `sudo apt install python3.7`
Discord.py: `python3.7 -m pip install -U discord.py`
Discord Voice: `python3.7 -m pip install -U discord.py[voice]`
Pip: `apt install python3-pip`
AIO Files: `python3.7 -m pip install aiofiles`
matplotlib: [[HERE]](https://matplotlib.org/3.0.3/users/installing.html)
NUMPY: `python3.7 -m pip install numpy`
NUMEXPR: ``python3.7 -m pip install numexpr`

#### Files
Once you have chosen a folder to keep the program in, be sure to do the above imports again in the folder, in case.

Then proceed to make the following text files, yes the names are important:

`PrismaticText` // `PrismaticM2M-R` // `PrismaticM2M-C` // `MathIn` // `MathOut` // `SciIn` // `SciOut` // `EngIn` // `EngOut`

Those text files represent seperate arrays, making it easy to see which stuff it learned

Once created, add your responses to `PrismaticText`, where each line represents a new response. If you want a multi-line response, use `\n`
