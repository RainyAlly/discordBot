import discord
from discord.ext import commands

CommandList = [
    "$help - Opens up a command list",
    "$hello - Introduces the bot",
    "$test - A *small* test to see if common text features work"
]

client = commands.Bot(command_prefix = '$', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("\n\n\n\n")
    print("GameJot is now online")
    print("\n\n\n\n")

@client.command()
async def help1(ctx):
    num = 1
    await ctx.send("Here's my commands")
    for i in CommandList:
        await ctx.send(f"{num}) {CommandList[num - 1]}")
        num = num + 1

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am GameJot")

@client.command()
async def ping(ctx):
    await ctx.send("1) \n# *Text*")

client.run('API KEY HERE')
