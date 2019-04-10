#Clean Poweroff
@bot.command()
@commands.is_owner()
async def pwr():
  await bot.logout()
  await bot.close()
  bot.aiosession.close()
