import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ton ping est de : {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await bot.say(embed=embed)

bot.run('MzkzNTAyNjUwNTUwNzE0Mzcx.DR2t_A.GY9NtTKb6MDI5thwEcRANo7ZSY4')
