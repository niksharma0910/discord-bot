import discord  # importing discorapp's API. Link =  https://discordpy.readthedocs.io/en/latest/api.html
from discord.ext import commands

client = commands.Bot(command_prefix='.')

# on_ready : inbuilt discord API's function to check bot is up.
@client.event
async def on_ready():
    print('Running...') # just a message to show on console that will let developer know bot is running.

# on_message : for when someone sends a message
@client.event
async def on_message(message):
    # checking 1. the message 2. the channel of message 3. author of the messsage so only particular person can use it
    if message.content.startswith('!newchallenge') and message.channel == client.get_channel(698794122894508043) and message.author.id == 629017996945391662 :
        await message.channel.send(read_first_line())  #calling function read_first_line()
        await message.channel.send("Hey @everyone, today's problem to solve. #KeepPracticing")

def read_first_line():
    
    with open('links.txt','r') as f:
        # reads first line of links.txt, which contains all links. One link per line.
        first_line = f.readline()
        # splitting links line by line. It will not contain first line 
        # as curson has moved to end of first line after above code.
        data = f.read().splitlines(True)
    with open('links.txt','w') as f:
        # updates links.txt. Deleting first line.
        f.writelines(data)
    with open('hist.txt.','a') as f:
        # appending the links that have been used and deleted to hist.txt.
        f.write(first_line )
    #return the first link
    return first_line   

client.run('YOUR_BOT_TOKEN HERE') #your bot's unique token
