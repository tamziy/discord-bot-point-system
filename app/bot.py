from dotenv import load_dotenv
import os
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'Message received: {message.content}') 
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('ozzo is fat')
        
    if message.content.startswith('!add points'):
        await message.channel.send('adding 5 points')

client.run(TOKEN)
