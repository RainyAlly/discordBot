import discord
from discord.ext import commands

BotName = "Discord Bot"

client = commands.Bot(command_prefix = '$', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("\n\n\n\n")
    print(f"{BotName} is now online")
    print("\n\n\n\n")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, I am {BotName}")

client.run('API KEY NOT HERE')
