import keep_live  # to keep the bot alive
import discord
# ext = extension
from discord.ext import commands
import os
from datetime import datetime

bot  = commands.Bot(command_prefix ='?')

bot.remove_command('help')
 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(bot.guilds)} Servers'))


@bot.command(aliases=["reload"])
async def re_load_ext(ctx, *name_of_ext):
    """To reload extension(s)"""

    if str(ctx.author.id) in ("740633806569996358", "759129467414380554"):
        try:
            for i in name_of_ext:
                bot.reload_extension(i)

        except Exception as err:
            await ctx.send(err)

        else:
            await ctx.send(f"{name_of_ext} was successfully reloaded")

    else:
        await ctx.send(f"You don't have perms <@{ctx.author.id}>, _ stupid just why are you a dick or somthing just why?_")

 
cogs = [f"cogs.{i[:-3]}" for i in os.listdir(".//cogs") if i[-3:] == ".py"]

for i in cogs:
    try:
        bot.load_extension(i)
    except Exception:
        print(i)

bot.run(os.environ.get("bot_token"))
