##/// GRAPHING
import numpy as np
import ast
import io
from ast import literal_eval
import matplotlib.pyplot as plt
@bot.command()
async def graph(ctx, eq, xmin, xmax):
    x = np.array(range(xmin, xmax))  
    y = ast.safe_eval(eq.replace("^", "**"))
    plt.plot(x, y)
    tempimg = io.bytesio(plt.show())
    await ctx.send(file=discord.File(tempimg))
