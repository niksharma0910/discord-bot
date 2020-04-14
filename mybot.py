import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.content.startswith('!newchallenge') and message.channel == client.get_channel(698794122894508043) and message.author.id == 629017996945391662 :
        await message.channel.send(read_first_line())
        await message.channel.send("Hey @everyone, today's problem to solve. #KeepPracticing")

def read_first_line():
    with open('links.txt','r') as f:
        first_line = f.readline()
        data = f.read().splitlines(True)
    with open('links.txt','w') as f:
        f.writelines(data)
    with open('hist.txt.','a') as f:
        f.write(first_line )
    return first_line

client.run('YOUR_BOT_TOKEN HERE')
