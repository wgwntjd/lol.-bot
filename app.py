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
async def 검색(ctx: discord.Message):
    nickname = ctx.content.split()[2]
    print(nickname)
    url = 'https://www.op.gg/summoner/userName=' + nickname
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')
    champion_str = ''

    game_item_list = bs_obj.find(
        "div", {"class": "GameItemList"}).findAll("div", {"class": "ChampionName"})
    for i in range(5):
        champion_str += game_item_list[i].text + "\n"

    ctx.send(champion_str)

if __name__ == "__main__":
    bot.run(token)
