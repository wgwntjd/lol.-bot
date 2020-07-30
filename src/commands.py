import discord
from discord.ext import commands
from .lib.search_user import get_recent_champion, get_recent_kda, get_recent_rating, get_recent_result, get_recent_types, get_tier, get_average_stats 

game = discord.Game("롤. 유호진 씨발련 어떻게 죽일지 생각 중")
bot = commands.Bot(command_prefix="롤. ", status=discord.Status.online, activity=game, help_command=None)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def 살인(ctx):
    await ctx.send("어떻게 유호진을 죽여드릴까요??")


@bot.command()
async def 전적(ctx, arg):
    username = urllib.parse.quote(arg.split(':')[0])  # username parsing
    avr_result = get_average_stats(username)  # average result returned
    try:  # list length parsing
        list_length = int(arg.split(':')[1])
    except:
        list_length = 5
