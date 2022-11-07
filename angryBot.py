import discord
from discord.utils import get
# Credentials
TOKEN = 'MTAzOTAxMzAzMTUzNzAyNTA3NA.GNqECC.Q1Lh68yB6iHXDnQ-TMll8_a6ZmDpMVL6Jiwed0'
# Create bot
#client = commands.Bot(command_prefix="!")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
# Startup Information
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_message(message):
    await message.add_reaction("😠")
    await message.add_reaction("😡")

client.run(TOKEN)