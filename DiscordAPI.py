import discord
from discord.ext import commands
from dotenv import dotenv_values
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)

config = dotenv_values(".env")

bot_token = config["BOT_TOKEN"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent recursion
    if message.author == client.user:
        return

    # Send greeting message
    await message.channel.send(f'Hello {message.author.name}!')

    # Process commands
    await bot.process_commands(message)


client.run(bot_token)

