import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user}')

# --- أمر الأوامر (-اوامر) ---
@bot.command(name='اوامر')
async def help_command(ctx):
    embed = discord.Embed(
        title="🤖 قائمة أوامر البوت التفاعلية",
        description="هذه هي جميع الأوامر المتاحة في البوت، استخدم البادئة (-) قبل أي أمر:",
        color=discord.Color.blue()
    )
    embed.add_field(name="📋 `-اوامر`", value="لعرض هذه القائمة التفاعلية ومساعدة الأعضاء.", inline=False)
    embed.add_field(name="📢 `-نداء`", value="لأغراض الإشراف والتواصل الإداري داخل السيرفر.", inline=False)
    embed.add_field(name="🎲 `-روليت`", value="بدء لعبة الروليت التفاعلية مع الأزرار وأرقام اللاعبين.", inline=False)
    embed.add_field(name="🏦 `-لوحة_بنك`", value="عرض النظام البنكي الافتراضي وكشف الحساب.", inline=False)
    embed.set_footer(text="تم تطوير البوت بنجاح.")
    await ctx.send(embed=embed)

@bot.command(name='نداء')
async def neda_command(ctx):
    await ctx.send(f"📢 تنبيه إداري بواسطة: {ctx.author.mention}")

@bot.command(name='لوحة_بنك')
async def bank_command(ctx):
    await ctx.send(f"🏦 **البنك المركزي الافتراضي**\nحسابك الحالي نشط ومستقر يا {ctx.author.mention}.")


# --- نظام لعبة الروليت بالأزرار (-روليت) ---
class RouletteView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.players = {}

        for i in range(1, 21):
            self.add_item(RouletteButton(i))

class RouletteButton(discord.ui.Button):
    def __init__(self, number: int):
        super().__init__(style=discord.ButtonStyle.secondary, label=str(number), custom_id=f"roulette_{number}")
        self.number = number

    async def callback(self, interaction: discord.Interaction):
        view: RouletteView = self.view

        for num, user in view.players.items():
            if user.id == interaction.user.id:
                await interaction.response.send_message(f"❌ أنت مسجل مسبقاً في الرقم **{num}**!", ephemeral=True)
                return

        if self.number in view.players:
            await interaction.response.send_message(f"❌ هذا الرقم مأخوذ بواسطة {view.players[self.number].mention}", ephemeral=True)
            return

        view.players[self.number] = interaction.user
        self.style = discord.ButtonStyle.success
        self.disabled = True

        embed = interaction.message.embeds[0]
        players_text = "\n".join([f"` {num} ` : {user.mention}" for num, user in sorted(view.players.items())])
        if not players_text:
            players_text = "لا يوجد لاعبين حتى الآن."

        embed.set_field_at(0, name=f"أرقام اللاعبين: ({len(view.players)}/20)", value=players_text, inline=False)
        
        await interaction.response.edit_message(embed=embed, view=view)

@bot.command(name='روليت')
async def roulette_game(ctx):
    embed = discord.Embed(
        title="🎲 لعبة الروليت",
        description=(
            "**طريقة اللعب:**\n"
            "1- اضغط على أحد الأزرار بالأسفل لاختيار الرقم الذي سيمثلك في اللعبة.\n"
            "2- ستُبدأ الجولة وسيتم اختيار لاعب عشوائي.\n"
            "3- يطرد اللاعب وتبدأ جولة جديدة، وعندما يُطرد جميع اللاعبين ويبقي لاعبان فقط، ستدور العجلة ويكون اللاعب المختار هو الفائز!"
        ),
        color=discord.Color.dark_embed()
    )
    embed.add_field(name="أرقام اللاعبين: (0/20)", value="لا يوجد لاعبين حتى الآن.", inline=False)
    
    view = RouletteView()
    await ctx.send(embed=embed, view=view)

bot.run('MTU3MTc3OTc3ODU1NjU5NjIyNA.GD2Evc.DegMNmP7PR8ZEGaykLfFyaMa4mPCAy8sZhUVx0')
