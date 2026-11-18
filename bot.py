import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'البوت اشتغل وصار أونلاين 24 ساعة: {bot.user}')

bot.run('MTU3MTc3OTc3ODU1NjU5NjIyNA.Gx2ErB.K8-zpU3NlhsVltYWPdklKijgSzJq3MKqnYNS0Q')
