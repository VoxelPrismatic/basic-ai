#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##////DEPENDENCIES
#// $ apt install python3-pip
#// $ python3 -m pip install -U https://github.com/Rapptz/discord.py/zipball/rewrite
#// $ python3 -m pip install aiofiles
#// $ python3 -m pip install -U discord.py[voice]
#-----------------

##/// STARTUP
import logging, discord, random, logging, aiofiles, datetime, time, asyncio, threading, queue, typing
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, MissingPermissions
from discord.voice_client import VoiceClient
bot = commands.Bot(command_prefix=";]")
bot.remove_command("help")
logging.basicConfig(level='INFO')
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
        time.sleep(.1) # Verifies the transfer is over (its small data [~200bytes] so this is adequate)
        print('CONTINUE')

##/// OUTPUT
@bot.listen()
async def on_ready():
    bot.remove_command("help")
    print('\n \n \n \n',bot.guilds,'\n',*[bot.get_all_channels()],'\n \n \nGG! !] PRIZ AI ;] [! // v',discord.__version__,'// RESTART - CTRL Z, [up], [enter]\n \n \n')
    channel = bot.get_channel(556247032701124650)
    await channel.purge(limit=1)
    await channel.send(f'```diff\n+]I\'m back online, boiz!\n-]However, due to testing, I may be offline very shortly\n+] Turned on: {str(datetime.datetime.now())}\n-] Turns Off at 9PM CST```')
    await bot.change_presence(activity=discord.Game(name='with Prisms and Voxels :D'))
    channel = 561673143996121116
    print(time.time())
    #vc = await channel.connect()
    FilesLoad('r')
    asyncio.ensure_future(ArraysLoad())

##/// TEXT I/O
@bot.listen()
async def on_message(message):
    if message.author ==  bot.user:
        return
    else:
        if message.content == ']help':
            await message.channel.send('```diff\n-] ERROR\n+] To see commands list, use ";]hlep"```')
            return
        if message.content.startswith(']')==True:
            #AI CODE GOES HERE

##/// COMMANDS

@bot.command(aliases=["help"])
async def hlep(ctx):
    await ctx.send('''```md
# !] PRIZ AI ;] [! COMMANDS LIST
 
] ";]hlep"
> Brings up this message :)
] ";]ping"
> Shows the ping time :L
] ";]slots"
> Slot machine :D
] ";]coin"
> A virtual coin flip 0.0
] ";]git"
> Shows the github/gitlab repo ;]
] ";]rng {x} {y}"
> Prints a random number from [x] to [y]
] ";]clr {x}"
> Clears [x] messages XD
] ";]usrinfo"
>  Shows your user info 0.0
] ";]dnd"
> Roles all dice from Dragons and Dungeons!
] ";]info"
> Shows additional info

# To see mod commands, use ";]hlepmod"
# To have a conversation, use "]{your text here}"
```''')

@bot.command(aliases=["helpmod"])
async def hlepmod(ctx):
    await ctx.send('''```md
# !] PRIZ AI ;] [! MOD STUFF
 
] ";]hlepmod"
> Brings up this message :)
] ";]ban {user} {delete days} {reason}"
> Bans a {user} and removes messages from {delete days} ago for a {reason}
] ";]kick {user}"
> Kicks a {user} from the server
] ";]clr {int}"
> Deletes a {int} amount of messages

# To see user commands, use ";]hlep"
# To have a conversation, use "]{your text here}"
```''')

@bot.command()
async def info(ctx):
    await ctx.send('```ini\n# PRIZ AI\nAn RNG based AI that compares strings... literally\nOriginally written for the TI84+CSE and adapted into a way better Discord Bot!```')

@bot.command()
async def ping(ctx):
    await ctx.send(f'```ini\n#] !] PONG ;] [!\n-] Ping Time: {bot.latency}s```')
    print('!] PING TIME')

@bot.command()
async def slots(ctx):
    slot = ["[X]","[Y]","[Z]","[1]","[2]","[3]","[0]","[V]","[U]","[@]","[%]","[#]"]
    slot1 = random.randint(0,len(slot)-1)
    slot2 = random.randint(0,len(slot)-1)
    slot3 = random.randint(0,len(slot)-1)
    if slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        await ctx.send(f'```diff\n-] {slot[slot1-1]}{slot[slot2-1]}{slot[slot3-1]}\n+]>{slot[slot1]}{slot[slot2]}{slot[slot3]}<\n-] {slot[slot1+1]}{slot[slot2+1]}{slot[slot3+1]}\n \n-] WIN!```')
    else: 
        await ctx.send(f'```diff\n-] {slot[slot1-1]}{slot[slot2-1]}{slot[slot3-1]}\n+]>{slot[slot1]}{slot[slot2]}{slot[slot3]}<\n-] {slot[slot1+1]}{slot[slot2+1]}{slot[slot3+1]}\n \n-] LOST```')
        await ctx.send(f'```diff\n-] {slot[slot1-1]}{slot[slot2-1]}{slot[slot3-1]}\n+]>{slot[slot1]}{slot[slot2]}{slot[slot3]}<\n-] {slot[slot1+1]}{slot[slot2+1]}{slot[slot3+1]}\n \n-] LOST```')
    print('!] SLOTS')

@bot.command()
async def coin(ctx, num: int):
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
    if y == 0: await ctx.send(f'```{outp}```')
    await ctx.send(f'```]HEAD // {hcnt}\n]TAIL // {tcnt}```')

@bot.command()
@commands.is_owner()
async def pwr(ctx):
    await ctx.send('```md\n#]SEE YA PEEPS```')
    channel =  bot.get_channel(556247032701124650)
    await channel.purge(limit=1)
    await bot.logout()
    await bot.close()

@bot.command()
async def git(ctx):
    await ctx.send('`]GITHUB PAGE` https://github.com/VoxelPrismatic/basic-ai/\n`]GITLAB PAGE` https://gitlab.com/VoxelPrismatic/basic-ai/')
    print('!] GITHUB/GITLAB')

@bot.command()
@has_permissions(manage_messages=True)
async def clr(ctx, arg: int):
    await ctx.channel.purge(limit=arg+1)
    print(f'CLEAR [{arg}]')

@bot.command()
async def rng(ctx, rngl: int, rngh: int):
    print(f'!] RNG BETWEEN {rngl} & {rngh}')
    await ctx.send(f'```diff\n-] RNG BETWEEN {rngl} & {rngh}\n+] {rand(rngl,rngh)}```')

@bot.command()
@has_permissions(manage_roles=True, ban_members=True)
async def ban(ctx, members: commands.Greedy[discord.Member],
              delete_days: typing.Optional[int] = 0, *,
              reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)

@bot.command()
async def usrinfo(ctx):
    await ctx.send(f'```USER // {ctx.author.name}\nNICK // {user.display_name}\nJOINED // {member.joined_at}\nCREATED // {user.created_at}\nDISCRIM // {user.discriminator}\nUSER ID // {user.id}```')
    await ctx.send(f'```ROLES // {[role.name.replace("@", "") for role in user.roles]}\nSTATUS // {user.status}\nUSER PFP // {user.avatar_url}```')

@bot.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(self, *members: discord.Member):
    for member in members: await self.bot.kick(member)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clrin(ctx, int1: int, Int2: int):
    clrh = min(int1, int2)
    clrl = max(int1, int2)
    await ctx.channel.purge(limit=2000, before=clrl, after=clrh)

@bot.command()
async def rngs(ctx, rngl: int, rngh: int, num: int):
    if num > 2000: 
        await ctx.send('```]To prevent spam, MAX = 2000```')
        num = 2000
    send = ""
    temp = 0
    ttl = []
    print(f'!] RNG BETWEEN {rngl} & {rngh}')
    for x in range(num):
        temp = random.randint(rngl,rngh)
        if len(f'{send}[{temp}] ')<=1994:
            send += f'{temp} '
            ttl.append(temp)
        else:
            await ctx.send(f'```{send}```')
            send = ""
    await ctx.send(f'```diff\n-] RNG BETWEEN {rngl} & {rngh}```')
    if len(send) != 0: await ctx.send(f'```{send}```')
    await ctx.send(f'```CNT // {len(ttl)}\nAVG // {sum(ttl)/len(ttl)}```')

@bot.command()
async def dnd(ctx):
    await ctx.send(f"```md\n# DND!\nD4 ~ {rand(1,4)}\nD6 ~ {rand(1,6)}\nD8 ~ {rand(1,8)}\nD10 ~ {rand(1,10)}\nD12 ~ {rand(1,12)}\nD20 ~ {rand(1,20)}\n```")

##/// ERRORS
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('```]SYNTAX ERROR```')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('```]NO SUCH COMMAND```')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('```]BOT PERMS ERROR```')
    if isinstance(error, MissingPermissions):
        await ctx.send('```]USER PERMS ERROR```')

##/// BOT SETTINGS
key = ''
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
