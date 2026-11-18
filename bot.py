import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user}')

@bot.command(name='اوامر')
async def ping(ctx):
    await ctx.send("البوت شغال ومتصل بنجاح!")

# حط التوكن الجديد هنا بدال الكلام اللي بين القوسين
bot.run('هنا_حط_التوكن_الجديد_بدون_مسافات')
