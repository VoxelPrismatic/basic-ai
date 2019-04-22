#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##////DEPENDENCIES
#// $ apt install python3-pip
#// $ python3 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite
#// $ python3 -m pip install aiofiles
#// $ python3 -m pip install -U discord.py[voice]
#-----------------

##/// STARTUP
import logging
import discord
import random
import atexit
import copy
import logging
import queue
import threading
import aiofiles
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix="[][][]") ##/// So the console isnt filled with shit
client = discord.Client()
#------------

BAN = [''] ##/// Put your custom bad words here

##/// OUTPUT
@bot.listen()
async def on_ready():
    print('\n \n \n \n',bot.guilds,'\n',*[bot.get_all_channels()],'\n \n \nGG! !] PRIZ AI ;] [! // v',discord.__version__,'// RESTART - CTRL Z, [up], [enter]\n \n \n')
    channel =  bot.get_channel([status text channel here])
    await channel.send('\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__\__ \n I\'m back online, boiz! \n However, due to testing, I may be offline very shortly')
    await bot.change_presence(activity=discord.Game(name='with Prisms and Voxels :D'))
    channel = [status voice channel here]
    vc = await channel.connect() #this is brokk rn
#-----------


##/// TEXT I/O
@bot.listen("on_message")
async def prisms(message):
    if message.author ==  bot.user:
        return
    else:
        if message.content.startswith(']')==True:
            message.content = message.content[1:]+" "
            stop = False
            for x in range(len(BAN)-1):
                if BAN[x] in message.content:
                    stop = True
            if stop == false:
                generic = str(message.content)
                print(message.content)
                if len(generic) > 200:
                    await message.channel.send('`]DONT SPAM PLS`')
                    message.content = message.content[:200]
                
                if " " in message.content:
                    if "https" not in message.content:
                        async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1:
                            M2M1 = await mm1.readlines()
                        async with aiofiles.open('PrismaticM2M-C', mode='r') as mm2:
                            M2M2 = await mm2.readlines()
                        async with aiofiles.open('PrismaticText', mode='r') as textR:
                            AI = await textR.readlines()
                        LOOP = 1
                        FOR = ""
                        LEN = len(AI)
                        for x in range(LEN-1):
                            if LOOP==1:
                                print(AI[x])
                                if message.content in AI[x]:
                                    if message.content != AI[x]:
                                        RESPONSE = FOR
                                        LOOP = 0
                                        await message.channel.send(AI[x])
                        ##/// TO DISCORD
                        #//M2M READ
                        if LOOP==1:
                            async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1a:
                                M2M1 = await mm1a.readlines()
                                y = 0
                                for x in range(len(M2M1)-1):
                                    if message.content in M2M1[x]:
                                        y = x
                                if y == 0:
                                    print(message.content,'[/] M2M1')
                                    async with aiofiles.open('PrismaticText', mode='r') as textR:
                                        AI = await textR.readlines()
                                        print(AI)
                                        OUT = random.choice(AI)
                                    await message.channel.send(OUT)
                                else: 
                                    await message.channel.send(M2M2[y])
                            ##/// LEARNING
                            if random.randint(0,3)==2: #// LEARN TEXT
                                async with aiofiles.open('PrismaticText', mode='r') as textR:
                                    AI = await textR.readlines()
                                    store = message.content+'\n'
                                    if message.content and store not in AI:
                                        async with aiofiles.open('PrismaticText', mode='a') as textW:
                                            await textW.write(message.content)
                                            await textW.write('\n')
                                            print('\n\n\nADDED [',message.content,']')
                                            print('WRITE')
                                        await message.channel.send('`]LEARN`')
                            ##///M2M WRITE
                            if random.randint(0,8)==8: #// M2M WRITE
                                async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1:
                                    M2M1 = await mm1.readlines()
                                    if message.content not in M2M1:
                                        async with aiofiles.open('PrismaticM2M-R', mode='a') as mm1:
                                            await mm1.write(message.content)
                                            await mm1.write('\n')
                                            print('\n\n\nM2M [',message.content,']')
                                            print('WRITE')
                                            await message.channel.send('`]M2M_1`')
                                        async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1:
                                            M2M1 = await mm1.readlines()
                                    async with aiofiles.open('PrismaticM2M-C', mode='r') as mm2:
                                        M2M2 = await mm2.readlines()
                                        if OUT not in M2M2:
                                            async with aiofiles.open('PrismaticM2M-C', mode='a') as mm2:
                                                await mm2.write(OUT)
                                                await mm2.write('\n')
                                                print('\n\n\nM2M [',OUT,']')
                                                print('WRITE')
                                                await message.channel.send('`]M2M_2`')
                                            async with aiofiles.open('PrismaticM2M-C', mode='r') as mm2:
                                                M2M1 = await mm2.readlines()
                else:
                    await message.channel.send('`]MUST HAVE SPACE`')
            else:
                await message.channel.send('`]WATCH YOUR LANGUAGE`')
            
##/// BOT SETTINGS
bot.run('[bot key here]')
