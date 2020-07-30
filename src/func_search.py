import urllib
import discord
from .lib.search_user import SearchUser

def get_profile_embed(arg):
    username = urllib.parse.quote(arg.replace(' ', '+'))  #username parsing
    su = SearchUser(username)

    average_stats = su.get_average_stats()

    embed=discord.Embed(title=su.get_user_name(), url="https://www.op.gg/summoner/userName=" + username, description=su.get_top_rank(), color=0x0475b8)
    embed.set_author(name=su.get_user_level() + "레벨")
    embed.set_thumbnail(url=su.get_user_icon())
    embed.add_field(name='개인/2인 랭크', value=su.get_tier()[0], inline=True)
    embed.add_field(name='\t|', value='\t|\n|\n', inline=True)
    embed.add_field(name='자유랭크', value=su.get_tier()[1], inline=True)
    embed.set_footer(text='최근 ' + average_stats[0] + '전 ' + average_stats[1] + '승 ' + average_stats[2] + '패\t승률 ' + average_stats[3])
    
    return embed

def get_qu_embed(arg):
    username = urllib.parse.quote(arg.split(':')[0]).replace(' ', '+')
    try:
        list_length = int(arg.split(':')[1])
        if list_length > 20:
            list_length = 20
    except:
        list_length = 5

    su = SearchUser(username)

    su.get_recent_result(list_length)
    game_result = su.get_recent_result(list_length)
    game_champ = su.get_recent_champion(list_length)
    game_KDA = su.get_recent_kda(list_length)
    game_types = su.get_recent_types(list_length)
    game_rating = su.get_recent_rating(list_length)

    qu_count, win_count, lose_count = 0, 0, 0
    qu_value, kda_value, type_value = '', '', ''
    type_dict = {"Normal": "일반", "Ranked": "개인/2인 랭크", "Flex": "자유 5:5 랭크",
    "Special":"특별게임모드", "ARAM":"무작위 총력전", "URF":"우르프", "Tutorial":"튜토리얼", "Bot":"봇전"}

    embed = discord.Embed(title=su.get_user_name(), url="https://www.op.gg/summoner/userName=" + username, description ='개인/2인랭 자유랭크\n%s %s' %(su.get_tier()[0], su.get_tier()[1]), color=0x0475b8)
    embed.set_thumbnail(url=su.get_user_icon())
    for i in range(list_length):
        if game_result[i] == 'Victory':
            qu_value += '승리\t' + game_champ[i] + '\n'
            win_count += 1
        elif game_result[i] == 'Defeat':
            qu_value += '패배\t' + game_champ[i] + '\n'
            lose_count += 1
        else:
            qu_value += '무승\t' + game_champ[i] + '\n'            
        kda_value += game_KDA[i] + ' ▷' + game_rating[i] + '\n'          
        type_value += type_dict[game_types[i]] + '\n'
        qu_count += 1

    embed.add_field(name=str(qu_count) + '전 ', value=qu_value, inline=True)
    embed.add_field(name=str(win_count) + '승 ' , value=kda_value, inline=True)
    embed.add_field(name=str(lose_count) + '패', value=type_value, inline=True)

    return embed