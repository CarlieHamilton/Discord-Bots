# I am trying to make a discord bot that helps you with basic programming thingies,
# in multiple languages, as a simple reference. 
import discord
from discord.ext import commands
import random
import math
from random import shuffle
import json
import js
import rb
import tokenkey

bot = commands.Bot(command_prefix='!')
prefix = "!"
learnCommand = "none"
learnResponse = "none"

TOKEN = tokenkey.bot_token

client = discord.Client()

@client.event
async def on_ready():
    print("A wild Bot appears")
#    await client.change_presence(activity=discord.activity(name="being all bot like"))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith(prefix + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith(prefix + 'js' + ' comment'):
        await message.channel.send(js.comment_answer)
    if message.content.startswith(prefix + 'js' + ' if'):
        await message.channel.send(js.if_answer)
    if message.content.startswith(prefix + 'rb' + ' print') or message.content.startswith(prefix + 'rb' + ' puts'):
        await message.channel.send(rb.print_answer)
    # if message.content.startswith('!learn'):
    #     global learnCommand
    #     learnCommand = message.content[7:]
    #     await message.channel.send("oh, you want me to learn \"" + learnCommand + "\" do you hmmmm?")
    # if message.content.startswith("!yes"):
    #     await message.channel.send("and what do you wish for me to say in response?")
    # if message.content.startswith("!response"):
    #     global learnResponse
    #     global json
    #     learnResponse = message.content[10:]
    #     await message.channel.send(learnResponse + " hmmmm?")
    #     await message.channel.send("alright, I'll consider it")
        # copybotdict.append({"botcommand": learnCommand, "botresponse": learnResponse})
        # jsonwrite = json.dumps(copybotdict)
        # p = open("dict.json", "w")
        # p.write(jsonwrite)

    # if message.content.startswith("!no"):
    #     await message.channel.send("wasting my time, hmmmm?")

    # for d in copybotdict:
    #     if message.content.startswith(prefix + d["botcommand"]):
    #         await message.channel.send(d["botresponse"])






client.run(TOKEN)