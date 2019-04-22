##/// REACT
@bot.command()
async def react(ctx, mID: int, *reactions):
    message = await ctx.fetch_message(mID)
    for reaction in reactions:
        try:
            await message.add_reaction(reaction)
        except discord.HTTPException: await exc(ctx, 1)
        except discord.Forbidden: await exc(ctx, 2)
        except discord.NotFound: await exc(ctx, 3)

##/// STATS
import statistics
@bot.command()
async def stats(ctx, *data: int):
    await ctx.send(embed=embedify(f'''```md
#] STATS
>   MAX // {max(data)}
>   MIN // {min(data)}
>   AVG // {mean(data)}
>   MOD // {mode(data)}
>   MED // {median(data)}
> RANGE // {max(data)-min(data)}
> STDEV // {stdev(data)}
> LOMED // {median_low(data)}
> HIMED // {median_high(data)}
```'''))

##/// UPDATED BLACKJACK
@bot.command()
async def blkjck(ctx):
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
            if stu == 1: usr = usr+heart.pop[temp]+' '
            elif stu == 2: usr = usr+spade.pop[temp]+' '
            elif stu == 3: usr = usr+diam.pop[temp]+' '
            elif stu == 3: usr = usr+club.pop[temp]+' '
            temp += 1
            if temp > 10: temp = 10
            ttl1 += temp
    while ttl2 <= 18:
        temp = rand(0,12)
        if temp + ttl2 + 1 != 21:
            if stu == 1: cpu = cpu+heart.pop[temp]+' '
            elif stu == 2: cpu = cpu+spade.pop[temp]+' '
            elif stu == 3: cpu = cpu+diam.pop[temp]+' '
            elif stu == 3: cpu = cpu+club.pop[temp]+' '
            temp += 1
            if temp > 10: temp = 10
            ttl2 += temp
    if ttl1 > 21: usrtxt = f'USER // {usr} [{ttl1}] [BUST]'
    elif ttl1 > ttl2: usrtxt = f'USER // {usr} [{ttl1}] [WIN]'
    elif ttl1 < ttl2: usrtxt = f'USER // {usr} [{ttl1}] [LOSS]'
    if ttl2 > 21: cputxt = f'COMP // {cpu} [{ttl2}] [BUST]'
    elif ttl2 > ttl1: cputxt = f'COMP // {cpu} [{ttl2}] [WIN]'
    elif ttl2 < ttl1: cputxt = f'COMP // {cpu} [{ttl2}] [LOSS]'
    if ttl1 == ttl2:
        usrtxt = f'USER // {usr} [{ttl1}] [TIE]'
        cputxt = f'COMP // {cpu} [{ttl2}] [TIE]'
    await ctx.send(f'```md\n#]BLACK JACK!\n \n{usrtxt}\n \n{cputxt}```')
