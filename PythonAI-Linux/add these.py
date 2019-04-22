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
