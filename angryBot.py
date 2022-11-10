from discord.ext import commands
import discord
from discord.utils import get
import json
import emojis

# Credentials
TOKEN = ''
# Create bot
#bot = commands.Bot(command_prefix="!")

intents = discord.Intents.all()
#intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents)
# Startup Information

## Current Server Info
current_server_index = -1
current_server_name = ""
current_server_id = 0
current_server_emojiList = ["😠", "😡"]

with open("serverInfo.json") as f:
    serverInfo = json.load(f)

@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    game = discord.Game('大怒神')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message):
    current_server_index = next((index for (index, d) in enumerate(serverInfo) if d["id"] == message.guild.id), None)
    current_server_name = message.guild.name
    current_server_id = message.guild.id
    current_server_emojiList = serverInfo[current_server_index]["emojiList"]
    for j in current_server_emojiList :
        await message.add_reaction(j)
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")
    
@bot.command()
async def test(ctx, msg, *args):
    arguments = ', '.join(args)
    await ctx.send(f"!Hi <@{ctx.author.id}>, Your message: {msg}, Your argument1: {arguments}")
    
@bot.command()
async def add(ctx, emojis):
    current_server_emojiList.append(emojis)
    await ctx.send(f"!Hi <@{ctx.author.id}>, Added Emoji: {emojis}")
    #serverInfo.append()
    #with open("serverInfo.json", "w", encoding="utf-8") as f:
    #    json.dump(serverInfo, f, ensure_ascii=False, indent=2)


#@bot.command()
#async def list(ctx):
#    emojis = ', '.join(emojiList)
#    await ctx.send(f"!Hi <@{ctx.author.id}>, Now emojis: {emojis}")

#@bot.command()
#async def del(ctx, emojis):
#    emojiList.append(emojis)
#    await ctx.send(f"!Hi <@{ctx.author.id}>, Added Emoji: {emojis}")

@bot.command()
async def emojiInfo(ctx):
    for emoji in ctx.guild.emojis:
        print(emoji.name, emoji.id) 

bot.run(TOKEN)
