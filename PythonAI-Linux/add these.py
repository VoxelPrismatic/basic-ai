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
> Rick Roll! °ω°``````md
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
    
@bot.command(aliases=["os"])
async def sys(ctx):
    embed = discord.Embed(title="!] PRIZ AI ;]", description=f'''
```diff
+] !] PRIZ AI ;] [! SYSTEM INFO``````

```''', color=0x069d9d)
    await ctx.send(embed=embed)
