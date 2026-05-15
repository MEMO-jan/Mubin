import discord
from discord.ext import commands

TOKEN = "MTUwNDc5NzA5NTA5MjAyNzQ5Mw.GRBq9k.uWXseBr4IBf90X52IZws3WgurEU8YdFQoYvITE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
