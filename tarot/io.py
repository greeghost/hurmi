from cards import Carte
import discord
from discord.ext import commands

def ask_move_cli(player):
    s = input("What would you want to play ?")
    s = s.replace(" ", "")
    print(s, s[:-1], s[-1])
    card_to_play = Carte(s[:-1], s[-1])

    f1 = 0
    for c in player.hand:
        if card_to_play == c:
            print("sounds good !")
            f1 = 1
    if not f1:
        print("you dirty cheater !")

async def ask_move_discord(player):
    ctx = player.dm_channel()
    if ctx == None:
        await ctx = player.create_dm()
    await ctx.send("What would you want to play ?")
    
