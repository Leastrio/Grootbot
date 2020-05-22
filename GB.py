import discord
from discord.ext import commands
import random
import asyncio

responses = ['I am Groot',
             'Groot',
             'I am not Groot',
             'We are Groot',
             'I am Groot?',
             'Am I Groot?',
             'i aM grooT',
             'Groot I am.',
             '🅸 🅰🅼 🅶🆁🅾🅾🆃',
             'Me am Groot',
             'Myself am Groot',
             'I am infact Groot',
             'https://tenor.com/view/dance-groot-guardians-of-the-galaxy-cute-gif-7201822',
             'https://tenor.com/view/baby-groot-dancing-gif-10722579']

triggers = ['groot',
            'Guardians of the galaxy',
            "Guardian's of the galaxy",
            'tree',
            'gr00t',
            'stickman',
            'stick man']

client = commands.Bot(command_prefix = "g!")

@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Guardians of the Galaxy"))

@client.event
async def on_message(msg):
    for word in triggers:
        if word.lower() in msg.content.lower() and not msg.author.bot:
            await msg.channel.send(random.choice(responses))
    await client.process_commands(msg)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


client.run('TOKEN')
