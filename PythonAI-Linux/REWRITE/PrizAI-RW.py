#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('##/// IMPORT ///##')
#/// DEPENDENCIES

import ast
import typing
import discord                    #python3.7 -m pip install -U discord.py
import logging
import numpy as np                #python3.7 -m pip install -U numpy
import numexpr as ne              #python3.7 -m pip install -U numexpr
import datetime, time
import aiofiles, io, asyncio      #python3.7 -m pip install -U aiofiles
import matplotlib.pyplot as pyplt #python3.7 -m pip install -U matplotlib // SEE SITE FOR MORE
import matplotlib, math, statistics, random
import platform, sys, sysconfig, traceback, shlex
from shlex import quote
from ast import literal_eval
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot, MissingPermissions, has_permissions
bot = commands.Bot(command_prefix=";]")
bot.remove_command("help")
logging.basicConfig(level='INFO')
with open('secrets.txt', mode='r') as KEY: secrets = KEY.readlines()

print('##///  DONE  ///##')

print('##/// IMPORT ///##')
import PrizAI_CODE
bot.load_extension('PrizAI_COM')
print('##///  DONE  ///##')

##///---------------------///##
##///   BOT DEFINITIONS   ///##
##///---------------------///##

print('##/// DEFINE ///##')

def FilesLoad(rw): #// Making life easy when the actual code comes
    global PrizM2MR, PrizM2MC, PrizTXT, PrizMATHl, PrizSCIl, PrizENGl, PrizMATHr, PrizSCIr, PrizENGr #Or this wont work at all
    PrizM2MR = aiofiles.open('PrismaticM2M-R', mode=rw)     #M2M Read File
    PrizM2MC = aiofiles.open('PrismaticM2M-C', mode=rw)     #M2M Send File
    PrizTXT = aiofiles.open('PrismaticText', mode=rw)       #Response Data
    PrizMATHl = aiofiles.open('MathIn', mode=rw)            #Learned Math Words
    PrizSCIl = aiofiles.open('SciIn', mode=rw)              #Learned Sci Words
    PrizENGl = aiofiles.open('EngIn', mode=rw)              #Learned Eng Words
    PrizMATHr = aiofiles.open('MathOut', mode=rw)           #Math Response
    PrizSCIr = aiofiles.open('SciOut', mode=rw)             #Sci Response
    PrizENGr = aiofiles.open('EngOut', mode=rw)             #Eng Response
    print('R/W TO FILES')
##/// Currently, the above is only used to READ data for the below section, but i'd rather have it now in case i need it later

async def ArraysLoad():
    global M2M1, M2M2, AI, MATHl, SCIl, ENGl, MATHr, SCIr, ENGr
    FilesLoad('r')
    async with PrizM2MR as mm1, PrizM2MC as mm2, PrizTXT as textR, PrizMATHl as math1R, PrizSCIl as sci1R, PrizENGl as eng1R, PrizMATHr as math2R, PrizSCIr as sci2R, PrizENGr as eng2R:
        M2M1 = await mm1.readlines()
        M2M2 = await mm2.readlines()
        AI = await textR.readlines()
        MATHl = await math1R.readlines()
        SCIl = await sci1R.readlines()
        ENGl = await eng1R.readlines()
        MATHr = await math2R.readlines()
        SCIr = await sci2R.readlines()
        ENGr = await eng2R.readlines()
        print('LOADED ARRAYS')

def embedify(text): return discord.Embed(title="!] PRIZ AI ;] [!", description=text, color=0x069d9d)

print('##///  DONE  ///##')

##///---------------------///##
##///      BOT LOOPS      ///##
##///---------------------///##

print('##// STARTING //##')

@bot.listen()
async def on_ready():
    print(time.time())
    FilesLoad('r')
    await ArraysLoad()
    print('If an error didn\'t show up yet, then all should be good')
    bot.locked = False
    print(f'''
{bot.guilds}

{[bot.get_all_channels()]}

GG! !] PRIZ AI ;] [! // v{discord.__version__}// RESTART - CTRL Z, [up], [enter]
''')
    channel = bot.get_channel(556247032701124650)
    await bot.change_presence(activity=discord.Activity(type=3, name='the Prisms fly by 0.0', url='https://discord.gg/Z84Nm6n'))
    await channel.purge(limit=10)
    await channel.send(embed=embedify(f'''```md
#] I\'M BACK ONLINE!!!
> All the Voxels are textured ;]
> I am still in the testing phase :C
> Watch me be entirely re-written 0.0
> Turned on: {str(datetime.datetime.now())} :D
#] Turns Off at 8PM CST XC```'''))

##///---------------------///##
##///      BOT EVENT      ///##
##///---------------------///##

@bot.listen()
async def on_message(bot, message):
    await PrizAI_CODE.on_message(message)

@bot.listen()
async def on_guild_join(bot, guild):
    await PrizAI_CODE.on_guild_join(guild)

@bot.listen()
async def on_guild_remove(guild):
    await PrizAI_CODE.on_guild_remove(guild)

@bot.listen()
async def on_command_error(bot, ctx, error):
    await ctx.send(f'```{PrizAI_CODE.on_command_error(ctx, error)}```')

@bot.listen()
async def on_error(bot, ctx, error):
    await PrizAI_CODE.on_error(event, *args, **kwargs)


##///---------------------///##
##///     OTHER STUFF     ///##
##///---------------------///##
key = secrets[0]
bot.run(key)
client.run(key)
