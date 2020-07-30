import asyncio
import discord
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from discord.ext import commands

# token
token_path = os.path.dirname(os.path.abspath(__file__)) + "/token.txt"
t = open(token_path, "r", encoding="utf-8")
token = t.read().split()[0]
print("Token_key: ", token)

game = discord.Game("롤. 유호진 씨발련 어떻게 죽일지 생각")
bot = commands.Bot(command_prefix="롤. ",
                   status=discord.Status.online, activity=game, help_command=None)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def 살인(ctx):
    await ctx.send("어떻게 유호진을 죽여드릴까요??")


@bot.command()
async def 검색(ctx, arg):
    nickname = arg.split()[0]
    try:
        list_length = arg.split()[1]
    except:
        list_length = 5
    print(nickname)

    url = 'https://www.op.gg/summoner/userName=' + nickname
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')
    profile_str = ''

    game_list = bs_obj.find("div", {"class": "GameItemList"})
    game_champ_list = game_list.findAll("div", {"class": "ChampionName"})
    game_KDA_list = game_list.select('div.KDA > div.KDA')

    for i in range(list_length):
        game_KDA = ''
        for j in game_KDA_list[i].text.split():
            game_KDA += j + " "
        print(game_KDA)
        profile_str += game_champ_list[i].text[:-1] + '\t' + game_KDA + "\n"

    print(profile_str)
    await ctx.send(profile_str)

if __name__ == "__main__":
    bot.run(token, bot=True, reconnect=True)
