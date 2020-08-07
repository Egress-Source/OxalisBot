import discord
import json
import time
import subprocess
from discord.ext import commands

supersecretstuff = json.loads(open("secrets.json").read())


client = commands.Bot(command_prefix="?")


@client.command()
async def status(ctx: commands.Context):
    await ctx.send(str(subprocess.run("papermc status | grep Status", stdout=subprocess.PIPE, shell=True).stdout, "utf-8"))


@client.command()
@commands.has_any_role(733773680147955833, 733558343209320470, 741095502791311410)
async def verify(ctx: commands.Context, member: discord.Member):
    if isinstance(member, discord.Member):
        guild: discord.Guild = ctx.guild
        await member.add_roles(guild.get_role(733558721736736810))
        await member.remove_roles(guild.get_role(734260573453418499))


@client.event
async def on_member_join(member: discord.Member):
    await member.add_roles(member.guild.get_role(734260573453418499))


client.run(supersecretstuff["token"])
