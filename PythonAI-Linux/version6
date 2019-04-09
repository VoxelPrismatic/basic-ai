#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##////DEPENDENCIES
#// $ apt install python3-pip
#// $ python3 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite
#// $ python3 -m pip install aiofiles
#// $ python3 -m pip install -U discord.py[voice]
#-----------------

##/// STARTUP
import logging, discord, random, logging, aiofiles, datetime, time, asyncio, threading, queue
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
logging.basicConfig(level='INFO')
bot = commands.Bot(command_prefix="[][][]")
client = discord.Client()
BAN = ["nigger","nig","faggot","fag","cunt","kike"]

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

def LoadNow(FileName):
    with open(FileName, mode='r') as shit:
        wtf = shit.readlines()
    time.sleep(.1) # Verifies the transfer is over (its small data [~1mb] so this is adequate)
    print('FORCE LOADED ARRAYS')
    return wtf

def LearnNow(File, MD, TxT, addtext): ##/// Instant Access (in case)
    with open(File, mode=MD) as CurrentText:
        CurrentText.write(TxT)
        CurrentText.write('\n')
        print(f'\n\n\n{addtext} [',TxT,']')
        print('WRITE')
        time.sleep(.2) # Verifies the transfer is over (its small data [~200bytes] so this is adequate)
        print('CONTINUE')

def Globalize():
    global M2M1, M2M2, AI, MATHl, SCIl, ENGl, MATHr, SCIr, ENGr, PrizM2MR, PrizM2MC, PrizTXT, PrizMATHl, PrizSCIl, PrizENGl, PrizMATHr, PrizSCIr, PrizENGr, PMath, PEng, PSci

##/// OUTPUT
@bot.listen()
async def on_ready():
    print('\n \n \n \n',bot.guilds,'\n',*[bot.get_all_channels()],'\n \n \nGG! !] PRIZ AI ;] [! // v',discord.__version__,'// RESTART - CTRL Z, [up], [enter]\n \n \n')
    channel =  bot.get_channel(556247032701124650)
    await channel.send(f'```diff\n+]I\'m back online, boiz!\n-]However, due to testing, I may be offline very shortly\n+] Turned on: {str(datetime.datetime.now())}\n-] Turns Off at 9PM CST```')
    await bot.change_presence(activity=discord.Game(name='with Prisms and Voxels :D'))
    channel = 561673143996121116
    #vc = await channel.connect()

##/// TEXT I/O
@bot.listen("on_message")
async def on_message(message):
    FilesLoad('r')
    asyncio.ensure_future(ArraysLoad())
    if message.author ==  bot.user:
        return
    else:
        if message.content.startswith(']')==True:
            message.content = message.content[1:]
            blank = False
            for z in range(0,len(message.content)-1):
                if message.content[0]==" " and blank == False:
                    message.content = message.content[1:]
                else:
                    blank == True
                    break

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
                if " " in message.content and "https" not in message.content:
                        LOOP = 1
                        AI = LoadNow('PrismaticText')
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
                            M2M1 = LoadNow('PrismaticM2M-R')
                            for x in range(len(M2M1)-1):
                                if message.content in M2M1[x]:
                                    y = x
                                    break
                            if y == 0:
                                print(message.content,'[/] M2M1')
                                async with aiofiles.open('PrismaticText', mode='r') as textR:
                                    AI = await textR.readlines()
                                    print(AI)
                                    OUT = random.choice(AI)
                                await message.channel.send(OUT)
                            else:
                                M2M2 = LoadNow('PrismaticM2M-C')
                                await message.channel.send(M2M2[y-1])
                            
                            
                            ##/// LEARNING
                            if random.randint(0,3)==2: #// LEARN TEXT
                                store = message.content+'\n'
                                words = message.content.split(" ")
                                HAS = PMath = PEng = PSci = 0
                                Globalize()
                                print(f"{MATHl}\n{ENGr}\n{SCIr}")
                                for word in words:
                                    for math in MATHl:
                                        if word in math:
                                            LearnNow('MathOut', 'a', message.content, 'MATHED')
                                            PMath += 1
                                            HAS = 1
                                for word in words:
                                    for text in ENGl:
                                        if word in text:
                                            LearnNow('EngOut', 'a', message.content, 'TYPED')
                                            PEng += 1
                                            HAS = 1
                                for word in words:
                                    for chem in SCIl:
                                        if word in chem:
                                            LearnNow('SciOut', 'a', message.content, 'EXPIRIMENTED')
                                            PSci += 1
                                            HAS = 1
                                Globalize()
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
                                                await message.channel.send('```]WHAT SUBJECT DOES THE FOLLOWING WORD BELONG TO?\n1] MATHS ">1"\n2] LANGUAGE ">2"\n3] SCIENCE ">3"\n4] GENERIC - anything else\n \nPlease wait 2 seconds before responding :D```'+word+'\n\_\_\_\_\_\_\_\_\_')
                                                time.sleep(2)
                                                
                                                user = await bot.wait_for('message')
                                                await message.channel.send('`]THX FAM!`')
                                                if ">1" in user.content:
                                                    LearnNow('MathIn', 'a', word, 'MATHED')
                                                    await message.channel.send('`]oOoOh Maths... :D`')
                                                elif ">2" in user.content:
                                                    LearnNow('EngIn', 'a', word, 'TYPED')
                                                    await message.channel.send('`]awww Languages... ;[`')
                                                elif ">3" in user.content:
                                                    LearnNow('SciIn', 'a', word, 'EXPIRIMENTED')
                                                    await message.channel.send('`]I will yote this and observe what happens... O.O`')
                                                elif word == words[len(words)-1]:
                                                    LearnNow('PrismaticText', 'a', word, 'ADDED')
                                                    await message.channel.send('`]LEARN`')
                                        
                                        
                            ##///M2M WRITE
                            if random.randint(0,8)==8: #// M2M WRITE
                                async with aiofiles.open('PrismaticM2M-R', mode='r') as mm1:
                                    M2M1 = await mm1.readlines()
                                    if message.content not in M2M1:
                                        if message.content+"\n" not in M2M1:
                                            LearnNow('PrismaticM2M-R', 'a', message.content, 'M2M1')
                                            await message.channel.send('`]M2M_1`')
                                            LearnNow('PrismaticM2M-C', 'a', message.content, 'M2M2')
                                            await message.channel.send('`]M2M_2`')
                                            
                else:
                    await message.channel.send('`]MUST HAVE SPACE`')
            else:
                await message.channel.send('`]WATCH YOUR LANGUAGE`')
            
##/// BOT SETTINGS
bot.run('botkeygoeshere')
