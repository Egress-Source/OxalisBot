import discord
import json
import time
import subprocess
from discord.ext import commands

supersecretstuff = json.loads(open("secrets.json").read())


client = commands.Bot(command_prefix="?")


@client.command()
'''Get Oxalis Minecraft server status'''
async def status(ctx: commands.Context):
    await ctx.send(str(subprocess.run("papermc status | grep Status", stdout=subprocess.PIPE, shell=True).stdout, "utf-8"))

client.run(supersecretstuff)
