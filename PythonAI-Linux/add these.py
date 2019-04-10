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

#Many RNG
@bot.command()
async def rng(ctx, rngl: int, rngh: int, count: int):
        send = ""
        temp = 0
        ttl = []
        print(f'!] RNG BETWEEN {rngl} & {rngh}')
        for x in range(count):
                temp = random.randint(rngl,rngh)
                if len(f'{send}[{temp}] ')=<1994:
                        send += f'{temp} '
                        ttl.append(temp)
                else:
                        await ctx.send(f'```]Due to Discord limitations, MAX = {x}... sry :C```')
                        break
        await ctx.send(f'```diff\n-] RNG BETWEEN {rngl} & {rngh}```')
        await ctx.send(f'```{send}```')
        await ctx.send(f'```CNT // {len(ttl)}\nAVG // {sum(ttl)/len(ttl)}```')
