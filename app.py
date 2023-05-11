import discord  
from discord.ext import commands 
import youtube_dl

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx, url: str):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("You need to be in a voice channel to use this command")
        return

    if ctx.voice_client:
        await ctx.voice_client.move_to(voice_channel)
    else:
        vc = await voice_channel.connect()