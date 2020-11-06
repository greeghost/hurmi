# hurmi.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from enum import Enum

class Suit(Enum):
    Pique = 'P'
    Coeur = 'C'
    Carreau = 'K'
    Trèfle = 'T'
    Atout = 'A'

class Height(Enum):
    As = '1'
    Deux = '2'
    Trois = '3'
    Quatre = '4'
    Cinq = '5'
    Six = '6'
    Sept = '7'
    Huit = '8'
    Neuf = '9'
    Dix = '10'
    Valet = 'V'
    Cavalier = 'C'
    Dame = 'D'
    Roi = 'R'


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='99', help='Does such a simple command really need a documentation ??')
async def neunundneunzig(ctx):
    await ctx.send("Luftballons !")

@bot.command(name='play')
async def get_card(ctx, height, suit = None):
    if suit == None:
        suit = Suit(height[1])
        height = Height(height[0])
    else:
        suit, height = Suit(suit), Height(height)
    await ctx.send(f"{height.name} de {suit.name}")


@bot.event
async def on_error(event, *args, **kwargs):
    with open('errors.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise



bot.run(TOKEN)
