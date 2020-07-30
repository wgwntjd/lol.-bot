import discord
from discord.ext import commands
from .func_search import get_profile_embed, get_qu_embed


game = discord.Game("롤. 유호진 씨발련 어떻게 죽일지 생각 중")
bot = commands.Bot(command_prefix=".", status=discord.Status.online, activity=game, help_command=None)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def 살인(ctx):
    await ctx.send("어떻게 유호진을 죽여드릴까요??")


@bot.command()
async def 프로필(ctx):  #game_result, champion_icon, user_KDA, user_rating, game_types
    msg_wait = await ctx.send("프로필 가져오는 중입니다...")
    try:
        embed = get_profile_embed(" ".join(ctx.message.content.split()[1:]))
        await msg_wait.delete()
    except Exception as e:
        await msg_wait.delete()
        await ctx.send("잘못된 입력입니다.")
        print(e)
        return
    await ctx.send(embed=embed)

@bot.command()
async def 전적(ctx):
    msg_wait = await ctx.send("전적 기록을 가져오는 중입니다...")
    try:
        embed = get_qu_embed(" ".join(ctx.message.content.split()[1:]))
        await msg_wait.delete()
    except Exception as e:
        await msg_wait.delete()
        await ctx.send("잘못된 입력입니다.")
        print(e)
        return
    await ctx.send(embed=embed)

