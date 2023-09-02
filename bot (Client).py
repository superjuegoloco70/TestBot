import discord
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith("$Flip a coin"):
        await message.channel.send(coin_flip())
    elif message.content.startswith("$Generate a password"):
        await message.channel.send(gen_pass(10))    
    elif message.content.startswith("$Help"):
        await message.channel.send(help())
    elif message.content.startswith('$deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()
client.run("")
