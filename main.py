import discord
from discrod.ext import commands

BotName = "Discord Bot"

client = comands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("\n\n\n\n")
    print(f"{BotName} is now online")
    print("\n\n\n\n")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, I am {BotName}")

client.run('{###   NEEDS TO HAVE A API KEY!!! WILL ADD TO THE HOST MACHINE   ###}')