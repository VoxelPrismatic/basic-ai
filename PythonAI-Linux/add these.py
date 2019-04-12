##/// ERRORS
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('```diff\n-]ERROR 400\n=]BAD ARGUMENT```')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('```diff\n-]ERROR 404\n=]COMMAND NOT FOUND```')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('```diff\n-]ERROR 503\n=]BOT FORBIDDEN```')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('```diff\n-]ERROR 403\n=]USER FORBIDDEN```')
    if isinstance(error, commands.ConversionError):
        await ctx.send('```diff\n-]ERROR 503\n=]UNAVAILABLE```')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('```diff\n-]ERROR 416\n=]MISSING ARGS```')
    if isinstance(error, commands.ArgumentParsingError):
        await ctx.send('```diff\n-]ERROR 418\n=]IM A TEAPOT```')
    if isinstance(error, commands.TooManyArguments):
        await ctx.send('```diff\n-]ERROR 429\n=]TOO MANY ARGS```')
    if isinstance(error, commands.DisabledCommand):
        await ctx.send('```diff\n-]ERROR 423\n=]LOCKED COMMAND```')
    if isinstance(error, commands.UserInputError):
        await ctx.send('```diff\n-]ERROR 409\n=]INPUTS CONFLICTING```')
    if isinstance(error, commands.NotOwner):
        await ctx.send('```diff\n-]ERROR 401\n=]UNAUTHORIZED```')
    if isinstance(error, commands.ExtensionError):
        await ctx.send('```diff\n-]ERROR 424\n=]FAILED EXTENSION```')
