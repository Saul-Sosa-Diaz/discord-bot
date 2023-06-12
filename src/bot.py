"""
file: bot.py
author: Saúl Sosa
date: 26/04/2023
description: This file contains the functions that are executed when the bot receives a command.
"""

import discord
from discord.ext import commands, tasks
from commands import *


def run_bot(API_KEY):

	class Bot(commands.Bot):
		def __init__(self, activity='la ruleta rusa con 6 balas.') -> None:
			intents = discord.Intents.all()
			super().__init__(command_prefix='_', intents=intents, activity=discord.Game(name=activity))
		

	bot = Bot()

	@bot.command()
	async def joke(ctx):
		await command_joke(ctx)

	@bot.command()
	async def play(ctx, url = None):
		await command_play(ctx, url)
	
	@bot.command()
	async def leave(ctx, url = None):
		await command_leave(ctx)
	
			

	bot.run(API_KEY)
  
    