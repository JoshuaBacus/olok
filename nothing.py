import discord
from discord.ext import commands
from threading import Thread
import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

def allowed(ctx):
    return ctx.author.id == 453110730464559105, 669735089571364905

bot = commands.Bot(command_prefix='a!')
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name= "Bumping Roblox Market!", type=1,)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: c!\n-----")
    print("I'am ready!")

@bot.command(name='auto-bump', aliases=['bump'])
@commands.check(allowed)
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            channel = bot.get_channel(int(channelid))
            await channel.send('@Nutz#0001 server can be bump!')           
            print(f'[AUTO-BUMP] Bump number: {count} sent')
            await asyncio.sleep(20)
        except Exception as e:
            print(f"[ERROR]: {e}")

bot.run("NzQxNDk4MTE3ODk5MTU3NTc1.Xy4b7w.eN8RLFyTkuJwQ4UYw2cDlKHROs0")
