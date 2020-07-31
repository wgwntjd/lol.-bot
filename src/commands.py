import discord
from discord.ext import commands
from .func_search import get_profile_embed, get_qu_embed, invite_bot, get_help


game = discord.Game("롤. 유호진 씨발련 어떻게 죽일지 생각 중")
bot = commands.Bot(command_prefix=".", status=discord.Status.online, activity=game, help_command=None)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def 봇초대(ctx):
    await ctx.send(embed=invite_bot())


@bot.command()
async def help(ctx):
    await ctx.send(embed=get_help())


@bot.command()
async def 프로필(ctx):  #game_result, champion_icon, user_KDA, user_rating, game_types
    msg_wait = await ctx.send("프로필 가져오는 중입니다...")
    try:
        username = " ".join(ctx.message.content.split()[1:])
        embed = get_profile_embed(username)
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

