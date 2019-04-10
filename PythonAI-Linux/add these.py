#Clean Poweroff
@bot.command()
@commands.is_owner()
async def pwr():
        await bot.logout()
        await bot.close()
        bot.aiosession.close()

#Clear Inbetween
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clrin(ctx, int1: int, Int2: int):
        clrh = min(int1, int2)
        clrl = max(int1, int2)
        await ctx.channel.purge(limit=2000, before=clrl, after=clrh)
