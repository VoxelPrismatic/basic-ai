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
