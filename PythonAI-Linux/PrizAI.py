#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##////DEPENDENCIES
#// $ apt install python3-pip
#// $ python3 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite
#// $ python3 -m pip install aiofiles
#// $ python3 -m pip install -U discord.py[voice]
#-----------------

##/// STARTUP
print('IMPORTING')
import logging
import discord
import random
import logging
import aiofiles
import datetime
import time
import asyncio
import math
import threading
import queue
import typing
import sysconfig
import platform
import ast
import io
import shlex
import matplotlib.pyplot as pyplt
import numpy as np
import numexpr as ne
from ast import literal_eval
from discord.ext import commands
from shlex import quote
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.voice_client import VoiceClient
print('DONE\nINITIALIZING')
bot = commands.Bot(command_prefix=";]")
bot.remove_command("help")
logging.basicConfig(level='INFO')
client = discord.Client()
flist = ""
BAN = ["idontfuckingcarejustno"]

print('DEFINING')

def FilesLoad(rw): #// Making life easy when the actual code comes
    global PrizM2MR, PrizM2MC, PrizTXT, PrizMATHl, PrizSCIl, PrizENGl, PrizMATHr, PrizSCIr, PrizENGr #Or this wont work at all
    PrizM2MR = aiofiles.open('PrismaticM2M-R', mode=rw) #M2M Read File
    PrizM2MC = aiofiles.open('PrismaticM2M-C', mode=rw) #M2M Send File
    PrizTXT = aiofiles.open('PrismaticText', mode=rw) #Response Data
    PrizMATHl = aiofiles.open('MathIn', mode=rw) #Learned Math Words
    PrizSCIl = aiofiles.open('SciIn', mode=rw) #Learned Sci Words
    PrizENGl = aiofiles.open('EngIn', mode=rw) #Learned Eng Words
    PrizMATHr = aiofiles.open('MathOut', mode=rw) #Math Response
    PrizSCIr = aiofiles.open('SciOut', mode=rw) #Sci Response
    PrizENGr = aiofiles.open('EngOut', mode=rw) #Eng Response
    print('R/W TO FILES')
##/// Currently, the above is only used to READ data for the below section, but i'd rather have it now in case i need it later

def rand(ll,tt): return random.randint(ll,tt)

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

async def LoadNow(FileName):
    async with aiofiles.open(FileName, mode='r') as shit:
        wtf = await shit.readlines()
    print('FORCE LOADED ARRAYS')
    return wtf

async def LearnNow(File, MD, TxT, addtext): ##/// Instant Access (in case)
    async with aiofiles.open(File, mode=MD) as CurrentText:
        await CurrentText.write(TxT)
        await CurrentText.write('\n')
        print(f'\n\n\n{addtext} [{TxT}]')
        print('WRITE')

async def LEARNnSEND(File, MD, TxT, addtext, sendhere, sendthis):
    async with aiofiles.open(File, mode=MD) as CurrentText:
        await CurrentText.write(TxT)
        await CurrentText.write('\n')
        print(f'\n\n\n{addtext} [{TxT}]')
        print('WRITE [LEARNnSEND]')
    await sendhere.send(sendthis)

async def SEND2(chnl, text1, text2):
    await chnl.send(text1)
    await chnl.send(text2)

async def exc(ctx, code: int):
    print('EXCEPTION!')
    if code == 1: await ctx.send('```diff\n-]ERROR 400\n=]BAD REQUEST```')
    elif code == 2: await ctx.send('```diff\n-]ERROR 403\n=]ALL FORBIDDEN```')
    elif code == 3: await ctx.send('```diff\n-]ERROR 404\n=]ALL NOT FOUND```')

print('DONE')

##/// OUTPUT
@bot.listen()
async def on_ready():
    print('\n \n \n \n',bot.guilds,'\n',*[bot.get_all_channels()],'\n \n \nGG! !] PRIZ AI ;] [! // v',discord.__version__,'// RESTART - CTRL Z, [up], [enter]\n \n \n')
    channel = bot.get_channel(556247032701124650)
    await channel.purge(limit=1)
    await channel.send(f'```md\n#] I\'m back online, boiz!\n> However, due to testing, I may be offline very shortly\n> Turned on: {str(datetime.datetime.now())}\n#] Turns Off at 9PM CST```')
    await bot.change_presence(activity=discord.Game(name='with Prisms and Voxels :D',url='https://discord.gg/Z84Nm6n'))
    channel = 561673143996121116
    print(time.time())
    #vc = await channel.connect()
    FilesLoad('r')
    await ArraysLoad()

@bot.listen()
async def on_message(message):
    if message.author ==  bot.user:
        return
    else:
        if message.content == "f":
            flist = f'```md\n#] TIME TO PAY RESPECTS\n> {message.author} PAID RESPECTS```'
            fmessage = await message.channel.send(flist)
            await fmessage.add_reaction('🇫')
        elif message.content == "ok":
            await message.channel.send('-MA 2019\nWait, are *you* MA?')
        elif message.content == ']help':
            await message.channel.send('```diff\n-] ERROR\n+] To see commands list, use ";]hlep"```')
            return
        elif message.content.startswith(']')==True:
            await ArraysLoad()
            message.content = message.content[1:]
            blank = False
            message.content = message.content.strip()
            print(message.content)
            if message.content == "":
                stop == True
            else:
                words = message.content.split(" ")
            stop = False
            for word in words:
                if word in BAN:
                    stop = True
                    break
            if blank == True:
                await message.channel.send('`]MUST NOT BE BLANK (otherwise i will break D: )`')
                stop = True

            if stop == False:
                generic = str(message.content)
                print(message.content)
                if len(generic) > 200:
                    await message.channel.send('`]DONT SPAM PLS`')
                    message.content = message.content[:200]
                if "https" not in message.content:
                        LOOP = 1
                        AI = await LoadNow('PrismaticText')
                        for MSG in AI:
                            print(MSG)
                            if message.content in MSG and message.content != MSG and message.content+"\n" != MSG:
                                await message.channel.send(MSG)
                                LOOP = 0
                                break

                        ##/// TO DISCORD
                        #//M2M READ
                        if LOOP==1:
                            y = 0
                            M2M1 = await LoadNow('PrismaticM2M-R')
                            for x in range(len(M2M1)-1):
                                if message.content in M2M1[x]:
                                    y = x
                                    break
                            if y == 0:
                                print(message.content,'[/] M2M1')
                                AI = await LoadNow('PrismaticText')
                                print(AI)
                                OUT = random.choice(AI)
                                await message.channel.send(OUT)
                            else:
                                M2M2 = await LoadNow('PrismaticM2M-C')
                                await message.channel.send(M2M2[y-1])
                            print(OUT)


                            ##/// LEARNING
                            if rand(0,5)==2: #// LEARN TEXT
                                store = message.content+'\n'
                                print(message.content)
                                words = message.content.split(" ")
                                HAS = PMath = PEng = PSci = 0
                                MATHl = await LoadNow('MathIn')
                                ENGl = await LoadNow('EngIn')
                                SCIl = await LoadNow('SciIn')
                                MATHr = await LoadNow('MathOut')
                                ENGr = await LoadNow('EngOut')
                                SCIr = await LoadNow('SciOut')
                                print(f"{MATHl}\n{ENGl}\n{SCIl}")
                                for word in words:
                                    for math in MATHl:
                                        if word in math:
                                            await LearnNow('MathOut', 'a', message.content, 'MATHED')
                                            PMath += 1
                                            HAS = 1
                                    for text in ENGl:
                                        if word in text:
                                            await LearnNow('EngOut', 'a', message.content, 'TYPED')
                                            PEng += 1
                                            HAS = 1
                                    for chem in SCIl:
                                        if word in chem:
                                            await LearnNow('SciOut', 'a', message.content, 'EXPIRIMENTED')
                                            PSci += 1
                                            HAS = 1
                                if PMath > PEng and PMath > PSci:
                                    await message.channel.send('`]This is mathy... i think :D`')
                                    await message.channel.send(random.choice(MATHr))
                                elif PEng > PMath and PEng > PSci:
                                    await message.channel.send('`]This is englishy... i presume :C`')
                                    await message.channel.send(random.choice(ENGr))
                                elif PSci > PMath and PSci > PEng:
                                    await message.channel.send('`]This is sciency... i hypothesise O.O`')
                                    await message.channel.send(random.choice(SCIr))
                                if message.content and store not in AI:
                                    if HAS == 0:
                                        for word in words:
                                            MSG = await message.channel.send(f'```diff\n+]WHAT SUBJECT DOES THE FOLLOWING WORD BELONG TO?\n-] MATHS ">1"\n-] LANGUAGE ">2"\n-] SCIENCE ">3"\n-] GENERIC - anything else\n \n=]Please a moment before responding :D```\n{word}\n\_\_\_\_\_\_\_\_\_')
                                            def check(m):
                                                return m.channel == message.channel and m.author == message.author
                                            user = await bot.wait_for('message', check=check)
                                            await user.channel.purge(limit=1)
                                            await MSG.edit(content="`]THX FAM`")
                                            if ">1" in user.content:
                                                await LEARNnSEND('MathIn', 'a', word, 'MATHED', user.channel,'`]oOoOh Maths... :D`')
                                            elif ">2" in user.content:
                                                await LEARNnSEND('EngIn', 'a', word, 'TYPED', user.channel, '`]awww Languages... ;[`')
                                            elif ">3" in user.content:
                                                await LEARNnSEND('SciIn', 'a', word, 'EXPIRIMENTED', user.channel, '`]I will yote this and observe what happens... O.O`')
                                            elif word == words[len(words)-1]:
                                                await LEARNnSEND('PrismaticText', 'a', message.content, 'ADDED', user.channel, '`]LEARN`')


                            ##///M2M WRITE
                            if random.randint(0,8)==8: #// M2M WRITE
                                async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1:
                                    M2M1 = await mm1.readlines()
                                    if message.content not in M2M1:
                                        if message.content+"\n" not in M2M1:
                                            await LEARNnSEND('PrismaticM2M-R', 'a', message.content, 'M2M1', message.channel, '`]M2M_1`')
                                            await LEARNnSEND('PrismaticM2M-C', 'a', message.content, 'M2M2', message.channel, '`]M2M_2`')

                else:
                    await message.channel.send('`]MUST HAVE SPACE`')
            else:
                await message.channel.send('`]WATCH YOUR LANGUAGE`')

##/// COMMANDS

@bot.command(aliases=["help"])
async def hlep(ctx):
    embed = discord.Embed(title="!] PRIZ AI ;]", description='''
```md
#] !] PRIZ AI ;] [! COMMANDS LIST``````md
] ";]hlep"
> Brings up this message :)
] ";]ping"
> Shows the ping time :L
] ";]slots"
> Slot machine :D
] ";]coin {x}"
> Flips a virtual coin {x} times 0.0 [{x} is optional]
] ";]git"
> Shows the github/gitlab repo ;]
] ";]rng {x} {y}"
> Prints a random number from {x} to {y}, {z} number of times (optional)
] ";]clr {x}"
> Clears [x] messages XD
] ";]usrinfo"
> Shows your user info 0.0
] ";]dnd"
> Roles all dice from Dragons and Dungeons!
] ";]info"
> Shows additional info
] ";]rick"
> Rick Roll! °ω°
] ";]bj"
> BLACKJACK! 0o0
] ";]spam {x}"
> Spams {x} amount of chars >.<
] ";]graph {eq} {xmin} {xmax}"
> Graphs {eq} from {xmin} to {xmax} [ymin and ymax are auto calc-d]
] ";]rto {x} {y}"
> Reduces the ratio of {x} and {y} ;-;
] ";]rad {x}"
> Reduces a radical, {x}! >:D``````md
#] To see mod commands, use ";]hlepmod"
#] To have a conversation, use "]{your text here}"
```''', color=0x069d9d)
    await ctx.send(embed=embed)

@bot.command(aliases=["helpmod"])
async def hlepmod(ctx):
    embed = discord.Embed(title="!] PRIZ AI ;]", description='''
```diff
-] !] PRIZ AI ;] [! MOD STUFF``````md
] ";]hlepmod"
> Brings up this message :)
] ";]ban {user} {delete days} {reason}"
> Bans a {user} and removes messages from {delete days} ago for a {reason}
] ";]kick {user}"
> Kicks a {user} from the server
] ";]clr {int}"
> Deletes a {int} amount of messages
] ";]clrin {messageID1} {messageID2}" # NOT WORKING
> Deletes messages between {messageID1} and {messageID2}``````diff
-] To see user commands, use ";]hlep"
-] To have a conversation, use "]{your text here}"
```''', color=0x069d9d)
    await ctx.send(embed=embed)

@bot.command(aliases=["system"])
async def sys(ctx):
    platform = str(sysconfig.get_platform())
    pyver = str(sysconfig.get_python_version())
    embed = discord.Embed(title="!] PRIZ AI ;]", description=f'''
```diff
+] !] PRIZ AI ;] [! SYSTEM INFO``````asciidoc
PLATFORM: {platform}
PYTHON: {pyver}
```''', color=0x069d9d)
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    try: await ctx.send('```ini\n# PRIZ AI\nAn RNG based AI that compares strings... literally\nOriginally written for the TI84+CSE and adapted into a way better Discord Bot!```')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def ping(ctx):
    try:
        await ctx.send(f'```ini\n#] !] PONG ;] [!\n-] Ping Time: {bot.latency}s```')
        print('!] PING TIME')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def slots(ctx):
    try:
        slot = ["[X]","[Y]","[Z]","[1]","[2]","[3]","[0]","[V]","[U]","[@]","[%]","[#]"]
        slot1 = rand(0,len(slot)-1)
        slot2 = rand(0,len(slot)-1)
        slot3 = rand(0,len(slot)-1)
        if slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            await ctx.send(f'```diff\n-] {slot[slot1-1]}{slot[slot2-1]}{slot[slot3-1]}\n+]>{slot[slot1]}{slot[slot2]}{slot[slot3]}<\n-] {slot[slot1+1]}{slot[slot2+1]}{slot[slot3+1]}\n \n-] WIN!```')
        else:
            await ctx.send(f'```diff\n-] {slot[slot1-1]}{slot[slot2-1]}{slot[slot3-1]}\n+]>{slot[slot1]}{slot[slot2]}{slot[slot3]}<\n-] {slot[slot1+1]}{slot[slot2+1]}{slot[slot3+1]}\n \n-] LOST```')
        print('!] SLOTS')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def coin(ctx, *nums: int):
    try:
        if len(nums) == 0:
            num = 1
        else:
            num = int(nums[0])
        tcnt = y = hcnt = 0
        outp = ""
        if num > 5000:
            await ctx.send('```]To prevent spam, MAX = 5000```')
            num = 5000
        print('!] COIN FLIP')
        for x in range(num):
            if rand(0,1) == 1:
                tcnt+=1
                outp = outp+"[T] "
            else:
                hcnt+=1
                outp = outp+"[H] "
            if y == 497:
                await ctx.send(f'```{outp}```')
                outp = ""
                y = 0
            else: y+=1
        if y != 0: await ctx.send(f'```{outp}```')
        await ctx.send(f'```]HEAD // {hcnt}\n]TAIL // {tcnt}```')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.is_owner()
async def pwr(ctx):
    try:
        await ctx.send('```md\n#]SEE YA PEEPS```')
        channel =  bot.get_channel(556247032701124650)
        await channel.purge(limit=1)
        await bot.logout()
        await bot.login()
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def git(ctx):
    try:
        await ctx.send('`]GITHUB PAGE` https://github.com/VoxelPrismatic/basic-ai/\n`]GITLAB PAGE` https://gitlab.com/VoxelPrismatic/basic-ai/')
        print('!] GITHUB/GITLAB')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@has_permissions(manage_messages=True)
async def clr(ctx, arg: int):
    try:
        await ctx.channel.purge(limit=arg+1)
        print(f'CLEAR [{arg}]')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.is_owner()
async def clr0(ctx, arg: int):
    try:
        await ctx.channel.purge(limit=arg+1)
        print(f'CLEAR [{arg}]')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def rng(ctx, rngl: int, rngh: int, *nums: int):
    try:
        if len(nums) == 0:
            num = 1
        else:
            num = int(nums[0])
        if num > 2000:
            await ctx.send('```]To prevent spam, MAX = 2000```')
            num = 2000
        send = ""
        temp = 0
        ttl = []
        await ctx.send(f'```diff\n-] RNG BETWEEN {rngl} & {rngh}```')
        print(f'!] RNG BETWEEN {rngl} & {rngh}')
        for x in range(num):
            temp = random.randint(rngl,rngh)
            if len(f'{send} {temp} ')<=1994:
                send += f'{temp} '
                ttl.append(temp)
            else:
                await ctx.send(f'```{send}```')
                send = ""
                send += f'{temp} '
                ttl.append(temp)
        if len(send) != 0: await ctx.send(f'```{send}```')
        await ctx.send(f'```COUNT // {len(ttl)}\nAVRGE // {sum(ttl)/len(ttl)}\nRANGE // {max(ttl)-min(ttl)}```')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, members: commands.Greedy[discord.Member],
              delete_days: typing.Optional[int] = 0, *,
              reason: str):
    for member in members:
        try:
            await member.ban
        except discord.HTTPException: await exc(ctx, 1)
        except discord.Forbidden: await exc(ctx, 2)
        except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def usrinfo(ctx):
    try:
        perms = '\n'.join(perm for perm, value in ctx.author.guild_permissions if value)
        await ctx.send(f'```USER // {ctx.author.name}\nNICK // {ctx.author.display_name}\nJOINED // {ctx.author.joined_at}\nCREATED // {ctx.author.created_at}\nDISCRIM // {ctx.author.discriminator}\n```')
        await ctx.send(f'```PERMS // {perms}\nSTATUS // {user.status}\nUSER PFP // {user.avatar_url}```')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(self, *members: discord.Member):
    for member in members:
        member = quote(member)
        try:
            await self.bot.kick(member)
        except discord.HTTPException: await exc(ctx, 1)
        except discord.Forbidden: await exc(ctx, 2)
        except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clrin(ctx, int1: int, int2: int):
    try:
        clrh = min(int1, int2)
        clrl = max(int1, int2)
        await ctx.channel.purge(limit=2000, before=clrl, after=clrh)
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.is_owner()
async def pin0(ctx, mID: int):
    try:
        message = await ctx.fetch_message(mID)
        await message.pin()
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.is_owner()
async def unpin0(ctx, mID: int):
    mID = quote(mID)
    try:
        message = await ctx.fetch_message(mID)
        await message.unpin()
        await ctx.send('`]UNPINNED`')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def pin(ctx, mID: int):
    try:
        message = await ctx.fetch_message(mID)
        await message.pin()
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unpin(ctx, mID: int):
    mID = quote(mID)
    try:
        message = await ctx.fetch_message(mID)
        await message.unpin()
        await ctx.send('`]UNPINNED`')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)


@bot.command()
@commands.is_owner()
async def clrin0(ctx, int1: int, Int2: int):
    try:
        clrh = min(int1, int2)
        clrl = max(int1, int2)
        await ctx.channel.purge(limit=2000, before=clrl, after=clrh)
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def dnd(ctx):
    try: await ctx.send(f"```md\n# DND!\nD4 ~ {rand(1,4)}\nD6 ~ {rand(1,6)}\nD8 ~ {rand(1,8)}\nD10 ~ {rand(1,10)}\nD12 ~ {rand(1,12)}\nD20 ~ {rand(1,20)}\n```")
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def rick(ctx):
    await ctx.send('Never gonna give you up!\nNever gonna let you down!\nNever gonna run around and, desert you!\nNever gonna make you cry!\nNever gonna say goodbye!\nNever gonna run around and, desert you!')

@bot.command()
async def calc(ctx, *, eq):
    msg = await ctx.send('`]CALCULATING`')
    eq = eq.strip().replace('^', '**').replace('x', '*')
    try:
        if '=' in eq:
            l = ne.evaluate(eq.split('=')[0], {"__builtins__": None}, {"sqrt": sqrt})
            r = ne.evaluate(eq.split('=')[1], {"__builtins__": None}, {"sqrt": sqrt})
            ans = str(l == r)
        else:
            ans = str(ne.evaluate(eq))
    except TypeError:
        return await ctx.send("`]SYNTAX ERROR`")
    await msg.delete()
    await ctx.send(f'`] {ans}`')

@bot.command()
async def graph(ctx, eq, xmin: int, xmax: int):
    msg = await ctx.send('`]GRAPHING`')
    try:
        x = np.array(range(xmin, xmax))
        y = ne.evaluate(eq.replace("^", "**"))
        fig = pyplt.figure()
        fig, ax = pyplt.subplots()
        ax.set_facecolor('#002823')
        ax.tick_params(labelcolor='#0000ff')
        pyplt.plot(x, y)
        fig.patch.set_facecolor('#002823')
        plotimg = io.BytesIO()
        pyplt.savefig(plotimg, format='png')
        plotimg.seek(0)
        await msg.delete()
        await ctx.send(file=discord.File(plotimg, 'img.png'))
        pyplt.close()
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

@bot.command()
async def cool(ctx, user: int):
    strtemp = '////////'
    await ctx.channel.purge(limit = 1)
    coolthing = await ctx.send(strtemp)
    varslol = True
    while varslol == True:
        try:
            for x in range(125):
                strtemp = f'{strtemp}////////'
                await coolthing.edit(content = f'{strtemp}')
            varslol = False
            await ctx.send(f'''
Never gonna give <@{user}> up!
Never gonna let <@{user}> down!
Never gonna run around, and, desert you!
Never gonna make <@{user}> cry!
Never gonna say goodbye!
Never gonna run around, and, desert you!
''')
        except:
            if varslol == False:
                await coolthing.edit(f'''
Never gonna give <@{user}> up!
Never gonna let <@{user}> down!
Never gonna run around, and, desert you!
Never gonna make <@{user}> cry!
Never gonna say goodbye!
Never gonna run around, and, desert you!
''')
            else:
                await ctx.send('YOU WILL NOT END THIS!')
                strtemp = '////////'
                coolthing = await ctx.send(strtemp)

@bot.command()
async def bj(ctx):
    heart = ['🂱','🂲','🂳','🂴','🂵','🂶','🂷','🂸','🂹','🂺','🂻','🂽','🂾']
    spade = ['🂡','🂢','🂣','🂤','🂥','🂦','🂧','🂨','🂩','🂪','🂫','🂭','🂮']
    diam = ['🃁','🃂','🃃','🃄','🃅','🃆','🃇','🃈','🃉','🃊','🃋','🃍','🃎']
    club = ['🃑','🃒','🃓','🃔','🃕','🃖','🃗','🃘','🃙','🃚','🃛','🃝','🃞']
    ttl1 = ttl2 = temp = stu = 0
    usr = cpu = cputxt = usrtxt = ""
    while ttl1 <= 18:
        temp = rand(0,12)
        if temp + ttl1 + 1 != 21:
            stu = rand(0,3)
            if stu == 1:
                usr = usr+heart[temp]+' '
                del heart[temp]
            elif stu == 2:
                usr = usr+spade[temp]+' '
                del spade[temp]
            elif stu == 3:
                usr = usr+diam[temp]+' '
                del diam[temp]
            elif stu == 3:
                usr = usr+club[temp]+' '
                del club[temp]
            temp += 1
            if temp > 10: temp = 10
            ttl1 += temp
    while ttl2 <= 18:
        temp = rand(0,12)
        if temp + ttl2 + 1 != 21:
            if stu == 1:
                cpu = usr+heart[temp]+' '
                del heart[temp]
            elif stu == 2:
                cpu = usr+spade[temp]+' '
                del spade[temp]
            elif stu == 3:
                cpu = usr+diam[temp]+' '
                del diam[temp]
            elif stu == 3:
                cpu == usr+club[temp]+' '
                del club[temp]
            temp += 1
            if temp > 10: temp = 10
            ttl2 += temp
    if ttl1 > 21:
        usrtxt = f'USER // {usr} [{ttl1}] [BUST]'
        cputxt = f'COMP // {cpu} [{ttl2}] [WIN]'
    elif ttl1 > ttl2:
        usrtxt = f'USER // {usr} [{ttl1}] [WIN]'
        cputxt = f'COMP // {cpu} [{ttl2}] [LOSS]'
    if ttl2 > 21:
        cputxt = f'COMP // {cpu} [{ttl2}] [BUST]'
        usrtxt = f'USER // {usr} [{ttl1}] [WIN]'
    elif ttl2 > ttl1:
        cputxt = f'COMP // {cpu} [{ttl2}] [WIN]'
        usrtxt = f'USER // {usr} [{ttl1}] [LOSS]'
    if ttl1 == ttl2:
        usrtxt = f'USER // {usr} [{ttl1}] [TIE]'
        cputxt = f'COMP // {cpu} [{ttl2}] [TIE]'
    await ctx.send(f'```md\n#]BLACK JACK!\n \n{usrtxt}\n \n{cputxt}```')

@bot.command()
async def spam(ctx, num: int):
    if num > 10000: num = 10000
    send = ""
    data = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcsdefghgijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{}\"\'<,>./?\\|`~"
    for x in range(num):
        send = send+(data[rand(0,len(data)-1)])
        if len(send) == 2000:
            await ctx.send(send)
            send = ""
    if len(send) > 0: await ctx.send(send)

@bot.command()
async def rto(ctx, int1: int, int2: int):
    factor = math.gcd(int1, int2)
    await ctx.send(f'```]FACT // {factor}\n]INT1 // {int1/factor}\n]INT2 // {int2/factor}```')

@bot.command()
async def rad(ctx, D: int):
    K = 1
    for I in range(1,500):
        for J in range(2,1000):
            if not math.remainder(D, J**2):
                D = D/(J**2)
                K = K*J
        if D == 1:
            break
    if K == 1: await ctx.send(f'```]ANS // √{D}```')
    elif D == 1: await ctx.send(f'```]ANS // {K}```')
    else: await ctx.send(f'```]ANS // {K}√{D}```')

@bot.command()
async def quad(ctx, A: int, B: int, C: int):
    D = B**2 - 4*A*C
    K = 1
    for I in range(1,500):
        for J in range(2,1000):
            if not math.remainder(D, J**2):
                D = D/(J**2)
                K = K*J
        if D == 1:
            break
    if K == 1: STR = f'√{D}'
    elif D == 1: STR = f'{K}'
    else: STR = f'{K}√{D}'
    await ctx.send(f'```md\n#]QUADRATICS``````\n{-B}+-{STR}\n------------\n{2*A}``````diff\n+] {(-B+((B**2)-2*A*C)**.5)/(2*A)}\n-] {(-B-((B**2)-2*A*C)**.5)/(2*A)}```')


##/// TO PAY RESPECTS
@bot.event
async def on_reaction_add(reaction,user):
    try:
        if str(user) not in reaction.message.content:
            if reaction.message.author == bot.user and user != bot.user:
                if 'PAID RESPECTS' in reaction.message.content:
                    await reaction.message.edit(content = f'```md{reaction.message.content[5:-3]}\n> {user} PAID RESPECTS```')
    except discord.HTTPException: await exc(ctx, 1)
    except discord.Forbidden: await exc(ctx, 2)
    except discord.NotFound: await exc(ctx, 3)

##/// ERRORS
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('```diff\n-]ERROR 400\n=]BAD ARGUMENT```')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('```diff\n-]ERROR 404\n=]COMMAND NOT FOUND```')
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send('```diff\n-]ERROR 503\n=]BOT FORBIDDEN```')
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send('```diff\n-]ERROR 403\n=]USER FORBIDDEN```')
    elif isinstance(error, commands.ConversionError):
        await ctx.send('```diff\n-]ERROR 503\n=]UNAVAILABLE```')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```diff\n-]ERROR 416\n=]MISSING ARGS```')
    elif isinstance(error, commands.ArgumentParsingError):
        await ctx.send('```diff\n-]ERROR 418\n=]IM A TEAPOT```')
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send('```diff\n-]ERROR 429\n=]TOO MANY ARGS```')
    elif isinstance(error, commands.DisabledCommand):
        await ctx.send('```diff\n-]ERROR 423\n=]LOCKED COMMAND```')
    elif isinstance(error, commands.NotOwner):
        await ctx.send('```diff\n-]ERROR 401\n=]UNAUTHORIZED```')
    elif isinstance(error, commands.ExtensionError):
        await ctx.send('```diff\n-]ERROR 424\n=]FAILED EXTENSION```')
    await ctx.send(f'```md\n#]>>> {error} <<<```')

##/// BOT SETTINGS
key = 'client secrets'
bot.run(key)
client.run(key)

"""
##/// OTHER NOTES (of importance?)
Available Permissions:
    create_instant_invite
    kick_members
    ban_members
    administrator
    manage_channels
    manage_guild
    add_reactions
    view_audit_log
    priority_speaker
    read_messages
    send_messages
    send_tts_messages
    manage_messages
    embed_links
    attach_files
    read_message_history
    mention_everyone
    external_emojis
    connect
    speak
    mute_members
    deafen_members
    move_members
    use_voice_activation
    change_nickname
    manage_nicknames
    manage_roles
    manage_webhooks
    manage_emojis
"""
