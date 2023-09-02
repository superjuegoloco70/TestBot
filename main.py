import discord, os, random, requests
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir("Kodland\Proyecto 2\imgs"))
    with open(f"Kodland\Proyecto 2\imgs/{img_name}", "rb") as f:
        picture = discord.File(f)
    await ctx.send (file = picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def coin(ctx):
    await ctx.send(coin_flip)

bot.run("")