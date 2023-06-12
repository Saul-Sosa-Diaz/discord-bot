"""
Autor: Saúl Sosa
Description: This file contains the functions that are executed when the bot receives a command.
Fecha: 12/06/2023
"""

import os
from jokeapi import Jokes # Import the Jokes class
import discord
from discord.ext import commands, tasks


async def get_joke():
	'''This is an asynchronous Python function that retrieves a random joke from a Jokes class instance and
	returns it as a single sentence or a setup and delivery.

	Returns
	-------
		The function `get_joke()` returns a string that contains a random joke. If the joke type is
	"single", the function returns the joke text. If the joke type is "twopart", the function returns
	the setup and delivery of the joke separated by a new line character.

	'''
	j = await Jokes()  # Initialise the class
	joke = await j.get_joke(category=['programming', 'dark', 'spooky'])  # Retrieve a random joke
	if joke["type"] == "single": # Print the joke
		return joke["joke"]
	else:
		return joke["setup"] + "\n" + joke["delivery"]



async def command_joke(ctx):
	'''This is an asynchronous Python function that sends a joke to a discord channel.

	Parameters
	----------
	ctx
		ctx stands for context and refers to the context in which the function is being called. In this
	case, it is likely that the function is being called within a Discord bot framework, and ctx would
	contain information about the message and channel where the command was invoked.

	'''   
	
	joke = await get_joke()
	await ctx.send(joke)


async def command_join(ctx):
	'''This function allows a user to join a voice channel in Discord using async Python.

	Parameters
	----------
	ctx
		ctx stands for context and is a parameter in Discord.py commands. It contains information about the
	message that triggered the command, such as the author, channel, server, and message content. It is
	used to access and manipulate information related to the message and the server.

	Returns
	-------
		a tuple containing the voice channel object and the voice client object after connecting to the
	voice channel.

	'''
	
	if not ctx.message.author.voice:
		await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
		return
	else:
		channel = ctx.message.author.voice.channel
	connect = await channel.connect()
	return channel, connect
	


async def command_leave(ctx):
	'''This Python function disconnects the bot from a voice channel if it is currently connected.
	
	Parameters
	----------
	ctx
		ctx stands for "context" and is a parameter commonly used in Discord.py commands. It contains
	information about the message that triggered the command, such as the author, channel, server, and
	message content. It allows the command to interact with the Discord API and perform actions such as
	sending messages, joining
	
	'''
	try:
		voice_client = ctx.message.guild.voice_client
		if voice_client is None:
			await ctx.send("The bot is not connected to a voice channel.")
		elif voice_client.is_connected():
			await voice_client.disconnect()
			await ctx.send("Goodbye, see yo!")

	except Exception as e:
		print(str(e))
		await ctx.send("Oops, it didn't go as expected, talk to Saul to fix it.")


async def command_play(ctx, url):
	'''This is a Python function that plays the audio of a YouTube video and displays a GIF in a Discord
	server.
	
	Parameters
	----------
	ctx
		ctx stands for context and is a parameter in Discord.py commands. It contains information about the
	message, server, channel, and user that triggered the command. It is used to access and manipulate
	various Discord objects and properties.
	url
		The URL of the YouTube video that the user wants to play as audio in the voice channel.
	
	Returns
	-------
		The function is not returning anything.
	
	'''
	try :
		if url is None:
			await ctx.send("Please provide a youtube link")
			return
		
		await command_join(ctx)
		server = ctx.message.guild
		voice_channel = server.voice_client
		
		gif_path = os.path.join(".", "images", "rickroll-roll.gif")  # Ruta del archivo GIF
		file = discord.File(gif_path, filename='rickroll-roll.gif')
		await ctx.send(file=file)
				
		
		filename =  os.path.join(".", "audio", "rickroll.mp3")
		voice_channel.play(discord.FFmpegPCMAudio(source=filename))

		voice_channel.disconnect()

	except Exception as e:
		print(str(e))
		await ctx.send("Oops, it didn't go as expected, talk to Saul to fix it.")