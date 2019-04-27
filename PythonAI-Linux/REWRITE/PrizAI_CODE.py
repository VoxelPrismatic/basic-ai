#!/usr/bin/env python3
# -*- coding: utf-8 -*

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
BAN = ["idontfuckingcarejustno"]
logging.basicConfig(level='INFO')
loggingchannel = bot.get_channel(569698278271090728)
print(f'>>>>> {loggingchannel} <<<<<')

##///---------------------///##
##///   BOT DEFINITIONS   ///##
##///---------------------///##

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

def com_err(code, text): return(f"```diff\n-] ERROR {code}\n=] {text}")
def rand(ll,tt): return random.randint(ll,tt)
def embedify(text): return discord.Embed(title="!] PRIZ AI ;] [!", description=text, color=0x069d9d)
def loop(string, array):
    rtrn = False
    for blank in array:
        if string in blank:
            rtrn = True; break
    return rtrn

async def log(head, text):
    loggingchannel = bot.get_channel(569698278271090728)
    msgs = await loggingchannel.send(embed=embedify(f'''```md\n#] {head}!\n> {text}```'''))
    return msgs

async def _io(TxT):
    msgs = await log("AI I/O", f'{TxT}')
    print(f']{TxT}')
    return msgs

async def com(command):
    msgs = await log("COMMAND USED", f'COMMAND // {command}')
    print(f']{command}')
    return msgs

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
    msgs = await _io('FORCE LOAD ARRAYS')
    try:
        async with aiofiles.open(FileName, mode='r') as shit: wtf = await shit.readlines()
        await msgs.add_reaction('👌')
    except: await _io('FAILURE')
    return wtf

async def LearnNow(File, MD, TxT, addtext): ##/// Instant Access (in case)
    msgs = await _io(f"{addtext} // {TxT}")
    try:
        async with aiofiles.open(File, mode=MD) as CurrentText: await CurrentText.write(f'{TxT}\n')
        await msgs.add_reaction('👌')
    except: await _io('FAILURE')

async def LEARNnSEND(File, MD, TxT, addtext, sendhere, sendthis):
    msgs = await _io(f"{addtext} // {TxT}")
    try:
        async with aiofiles.open(File, mode=MD) as CurrentText: await CurrentText.write(f'{TxT}\n')
        await msgs.add_reaction('👌')
    except: await _io('FAILURE')

async def SEND2(chnl, text1, text2): await chnl.send(text1); await chnl.send(text2)

async def exc(ctx, code: int):
    await log('EXCEPTION!',f'TYPE // {code}\n> OCCURED IN // {ctx.channel}\n> 1] BadReq // 2] AllForbid // 3] 404')
    if code == 1: await ctx.send('```diff\n-]ERROR 400\n=]BAD REQUEST```')
    elif code == 2: await ctx.send('```diff\n-]ERROR 403\n=]ALL FORBIDDEN```')
    elif code == 3: await ctx.send('```diff\n-]ERROR 404\n=]ALL NOT FOUND```')

##///---------------------///##
##///     THE AI BITS     ///##
##///---------------------///##

async def on_message(message):
    if message.author ==  bot.user: return
    else:
        if message.content == "f":
            fmessage = await message.channel.send(f'```md\n#] TIME TO PAY RESPECTS\n> {message.author} PAID RESPECTS```')
            await fmessage.add_reaction('🇫')
        elif message.content == "ok": await message.add_reaction('👌')
        elif message.content == ']help': await message.channel.send('```diff\n-] ERROR\n+] To see commands list, use ";]hlep"```')
        elif message.content.startswith(']')==True:
            await ArraysLoad()
            message.content = message.content[1:].strip(); blank = stop = False
            print(message.content)
            if message.content == "": stop == True
            else: words = message.content.split(" ")
            for word in words:
                if loop(word, BAN): stop = True
            if blank == True: await message.channel.send('`]MUST NOT BE BLANK (otherwise i will break D: )`')
            elif stop == False:
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
                                LOOP = 0; break

                        ##/// TO DISCORD
                        #//M2M READ
                        if LOOP==1:
                            y = 0
                            M2M1 = await LoadNow('PrismaticM2M-R')
                            for x in range(len(M2M1)-1):
                                if message.content in M2M1[x]: y = x; break
                            if y == 0:
                                print(message.content,'[/] M2M1')
                                AI = await LoadNow('PrismaticText')
                                print(AI)
                                OUT = random.choice(AI)
                                await message.channel.send(OUT)
                                print(OUT)
                            else:
                                M2M2 = await LoadNow('PrismaticM2M-C')
                                await message.channel.send(M2M2[y-1])

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
                                    if loop(word, MATHl):
                                        await LearnNow('MathOut', 'a', message.content, 'MATHED')
                                        PMath += 1; HAS = 1
                                    if loop(word, ENGl):
                                        await LearnNow('EngOut', 'a', message.content, 'TYPED')
                                        PEng += 1; HAS = 1
                                    if loop(word, SCIl):
                                        await LearnNow('SciOut', 'a', message.content, 'EXPIRIMENTED')
                                        PSci += 1; HAS = 1
                                if PMath > PEng and PMath > PSci:
                                    await SEND2(message.channel, '`]This is mathy... i think :D`', random.choice(MATHr))
                                elif PEng > PMath and PEng > PSci:
                                    await SEND2(message.channel, '`]This is englishy... i presume :C`', random.choice(ENGr))
                                elif PSci > PMath and PSci > PEng:
                                    await SEND2(message.channel, '`]This is sciency... i hypothesise O.O`', random.choice(SCIr))
                                if message.content and store not in AI and HAS == 0:
                                    for word in words:
                                        MSG = await message.channel.send(f'''```diff
+]WHAT SUBJECT DOES THE FOLLOWING WORD BELONG TO?
-] MATHS ">1"
-] LANGUAGE ">2"
-] SCIENCE ">3"
-] GENERIC - anything else
=]Please a moment before responding :D```
{word}
\_\_\_\_\_\_\_\_\_''')
                                        def check(m): return m.channel == message.channel and m.author == message.author
                                        user = await bot.wait_for('message', check=check)
                                        await user.channel.purge(limit=1)
                                        await MSG.edit(content="`]THX FAM`")
                                        if ">1" in user.content:
                                            await LEARNnSEND('MathIn', 'a', word, 'MATHED', user.channel,'`]oOoOh Maths... :D`')
                                        elif ">2" in user.content:
                                            await LEARNnSEND('EngIn', 'a', word, 'TYPED', user.channel, '`]awww Languages... ;[`')
                                        elif ">3" in user.content:
                                            await LEARNnSEND('SciIn', 'a', word, 'EXPIRIMENTED', user.channel, '`]I will yote this and observe what happens... O.O`')
                                        elif word == words[len(words)]: await LEARNnSEND('PrismaticText', 'a', message.content, 'ADDED', user.channel, '`]LEARN`')

                            ##///M2M WRITE
                            if random.randint(0,8)==8: #// M2M WRITE
                                M2M1 = await LoadNow('PrismaticM2M-R')
                                if message.content not in M2M1 and message.content+"\n" not in M2M1:
                                    await LEARNnSEND('PrismaticM2M-R', 'a', message.content, 'M2M1', message.channel, '`]M2M_1`')
                                    await LEARNnSEND('PrismaticM2M-C', 'a', message.content, 'M2M2', message.channel, '`]M2M_2`')

                else: await message.channel.send('`]DONT SEND LINKS`')
            else: await message.channel.send('`]WATCH YOUR LANGUAGE`')

##///---------------------///##
##///     EVENT CALLS     ///##
##///---------------------///##

async def on_guild_join(guild): await log("GUILD JOIN", f"SERVER // {guild}")
async def on_guild_remove(guild): await log("GUILD LEFT", f"SERVER // {guild}")

##///---------------------///##
##///     ERROR CALLS     ///##
##///---------------------///##

async def on_error(event, *args, **kwargs):
    async def on_error(event, *args, **kwargs):
        t, exception, info = sys.exc_info()
        await handler("EVENT FAILED", exception, event, None, None, *args, **kwargs)

async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('```diff\n-]ERROR 400\n=]BAD ARGUMENT```')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('🇫')
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
    else:
        await handler("COMMAND FAILURE", error.original, ctx=ctx)
        await ctx.send("""```md
#] GG MATE, YOU FUCKED IT UP
> But that's okay, cuz you breaking shit
> is how I can get better at preventing
> that from happening... :D```""")

async def handler(exception_type, exception, event=None, message=None, ctx = None, *args, **kwargs):
        if message is None and event is not None and hasattr(event, "message"): message = event.message
        if message is None and ctx is not None: message = ctx.message
        kwarg_info = arg_info = ""
        for arg in list(args): arg_info += extract_info(arg) + "\n"
        if arg_info == "": arg_info = "No arguments"
        for name, arg in kwargs.items(): kwarg_info += "{}: {}\n".format(name, extract_info(arg))
        if kwarg_info == "": kwarg_info = "No keyword arguments"
        try:
            await log("GG MATE, SOMEBODY FUCKED IT ALL UP!",f"""TYPE // {exception_type}
#>>>>>>>> ALL  INFO <<<<<<<<#
#//////// EXCEPTION ////////#
{str(exception)} [{type(exception)})]
-
#////////    ARG    ////////#"
{arg_info}
-
#////////   KWARG   ////////#
{kwarg_info}
-
#/////// STACK TRACE ///////#
{"".join(traceback.format_tb(exception.__traceback__))}
-
#////////   NAMES   ////////#
{event}
-
#////////  COMMAND  ////////#
   NAME // {ctx.command.name}
CHANNEL // {'Private Message' if isinstance(ctx.channel, PrivateChannel) else f"{ctx.channel.name} [`{ctx.channel.id}`]"}
   USER // {str(ctx.author)} [`{ctx.author.id}`]
""")
            await log("GG MATE, SOMEBODY FUCKED IT ALL UP!",f"""See the message 0.0
#////////  OG  MSG  ////////#
///>  {message.content}  <///
///]  {extract_info(message)}  [///
""")
        except Exception as exc:
            await log("SOMETHING IS SERIOUSLY FUCKED UP", f"ERROR // {exc}")