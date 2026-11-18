import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'البوت اشتغل وصار أونلاين: {bot.user}')

@bot.command(name='اوامر')
async def ping(ctx):
    await ctx.send("البوت متصل وجاهز!")

bot.run('MTU3MTc3OTc3ODU1NjU5NjIyNA.GD2Evc.DegMNmP7PR8ZEGaykLfFyaMa4mPCAy8sZhUVx0')
