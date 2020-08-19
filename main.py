import discord
import json
import time
import subprocess
from discord.ext import commands

supersecretstuff = json.loads(open("secrets.json").read())


client = commands.Bot(command_prefix=("?", "!"))


@client.command()
async def status(ctx: commands.Context):
    """Get Oxalis Minecraft server status"""
    await ctx.send(str(subprocess.run("papermc status | grep Status", stdout=subprocess.PIPE, shell=True).stdout, "utf-8"))


@client.command()
@commands.has_any_role(733773680147955833, 733558343209320470, 741095502791311410)
async def verify(ctx: commands.Context, member: discord.Member, username=None):
    """Verify a member"""
    print('check point a')
    if isinstance(member, discord.Member):
        print('check point b')
        guild: discord.Guild = ctx.guild
        print('check point alpha')
        await member.add_roles(guild.get_role(733558721736736810))
        print('check point beta')
        await member.remove_roles(guild.get_role(734260573453418499))
        print('check point gamma')
        if username != None:
            print('check point c')
            subprocess.run("papermc command whitelist add " + str(username), shell=True).stdout, "utf-8"
            await ctx.send(f"```Verified: Added {username} to whitelist!```")
        else:
            print('check point d')
            await ctx.send(f"```Verified: No username provided!```")
    else:
        print('check point e')
        await ctx.send(f"```Critical Error: Discord member does not exist!```")


@client.command()
@commands.has_any_role(733773680147955833, 733558343209320470, 741095502791311410)
async def whitelist(ctx: commands.Context, username):
    subprocess.run("papermc command whitelist add " + str(username), shell=True).stdout, "utf-8"
    await ctx.send(f"```Added {username} to whitelist!```")


@client.event
async def on_member_join(member: discord.Member):
    await member.add_roles(member.guild.get_role(734260573453418499))


client.run(supersecretstuff["token"])
