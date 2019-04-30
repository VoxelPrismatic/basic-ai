##/// MATH MODULE
@commands.command()
async def lawsin(typ: int, var1: decimal, var2: decimal, var3: decimal)
    
    
##/// HELP COMMAND UPDATE
async def help(ctx):
    result = 0
    def check(reaction, user): return user == ctx.author
    lit = ["""
] ";]hlep"
> Brings up this message :)
] ";]sys"
> Shows some sys info :P
] ";]ping"
> Shows the ping time :L
] ";]slots"
> Slot machine :D
] ";]coin {x}" [Option: {x}]
> Flips a virtual coin {x} times 0.0""",
                """] ";]git"
> Shows the github/gitlab repo ;]
] ";]rng {x} {y} {z}" [Option: {z}]
> Prints an RNG from {x} to {y}, {z} times
] ";]usrinfo"
> Shows your user info 0.0
] ";]dnd"
> Roles all dice from Dragons and Dungeons!
] ";]info"
> Shows additional info""",
                """] ";]cool {uID}"
> Gives someone [{userID}] a sneaky surpise ;D
] ";]rick"
> Rick Roll! °ω°
] ";]blkjck"
> BLACKJACK! 0o0
] ";]spam {x}"
> Spams {x} amount of chars >.<
] ";]graph {eq} {xmin} {xmax}"
> Graphs {eq} from {xmin} to {xmax} 9.6""",
                """] ";]rto {x} {y}"
> Reduces the ratio of {x} and {y} ;-;
] ";]rad {x}"
> Reduces a radical, {x}! >:D
] ";]react {mID} {reactions}" [{reaction}.split " "]
> Adds {reactions} to a given {mID} .-.
] ";]stats {data}"
> Gives stats given {data} ._.
] ";]quad {a} {b} {c}"
> Uses {a}, {b}, and {c} to solve the Quad Formula 0o0"""]
    msg = await ctx.send(embed=embedify(f'''```md
#] !] PRIZ AI ;] [! COMMANDS LIST``````md
{lit[result]}`````md
#] To see mod commands, use ";]hlepmod"
#] To have a conversation, use "]{your text here}""
#] Some of your data is stored, use ";]data" to see more
```'''))
    await msg.add_reaction('⏪')
    await msg.add_reaction('◀')
    await msg.add_reaction('⏹')
    await msg.add_reaction('▶')
    await msg.add_reaction('⏩')
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError: return await msg.clear_reactions()
        else:
            if str(reaction.emoji) == '⏪':
                result = 0
                await msg.remove_reaction('⏪', ctx.author)
                await msg.edit(embed=embedify(f'''```md
#] !] PRIZ AI ;] [! COMMANDS LIST``````md
{lit[result]}`````md
#] To see mod commands, use ";]hlepmod"
#] To have a conversation, use "]{your text here}"
#] Some of your data is stored, use ";]data" to see more
```'''))
            elif str(reaction.emoji) == '◀':
                await msg.remove_reaction('◀', ctx.author)
                if result == 0: return
                else: result = result - 1
            elif str(reaction.emoji) == '⏹':
                return await msg.clear_reactions()
            elif str(reaction.emoji) == '▶':
                await msg.remove_reaction('▶', ctx.author)
                if result == (len(m.pages) - 1): return
                else: result += 1
            elif str(reaction.emoji) == '⏩':
                result = len(m.pages) - 1
                await msg.remove_reaction('⏩', ctx.author)
            await msg.edit(embed=embedify(f'''```md
#] !] PRIZ AI ;] [! COMMANDS LIST``````md
{lit[result]}`````md
#] To see mod commands, use ";]hlepmod"
#] To have a conversation, use "]{your text here}"
#] Some of your data is stored, use ";]data" to see more
```'''))
