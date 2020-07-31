import urllib
import discord
from .lib.search_user import SearchUser

def invite_bot():
    client_id = 737977514324000858
    git_hub_url = 'https://github.com/wgwntjd/lol.-bot'
    github_icon = 'https://cdn.icon-icons.com/icons2/844/PNG/512/Github_icon-icons.com_67091.png'
    embed = discord.Embed(title="롤점하나 봇을 다른 서버에도 추가하고 싶다면 눌러주세요!", url="https://discord.com/oauth2/authorize?client_id={0}&scope=bot".format(client_id), color=0x0475b8)
    embed.set_author(name='development github', url=git_hub_url, icon_url=github_icon)

    return embed

def get_help():
    git_hub_url = 'https://github.com/wgwntjd/lol.-bot'
    github_icon = 'https://cdn.icon-icons.com/icons2/844/PNG/512/Github_icon-icons.com_67091.png'
    embed = discord.Embed(title="롤점하나 명령어 목록", color=0x0475b8)
    embed.set_author(name='development github', url=git_hub_url, icon_url=github_icon)
    embed.add_field(name='.프로필 (소환사명)', value="소환사의 프로필을 가져옵니다.", inline=False)
    embed.add_field(name='.전적 (소환사명):(판수)', value="소환사의 전적을 가져옵니다.\n만약 판수를 기입하지 않는다면 기본값으로 5판의 전적을 가져옵니다.", inline=False)
    embed.add_field(name='.봇초대', value="다른 서버에서 봇점하나 봇을 사용하고 싶다면\n링크를 클릭한뒤 봇을 초대할 서버를 선택해주세요.", inline=False)
    embed.set_footer(text="깃허브 star은 개발자들에게 힘이 됩니다.")
    
    return embed

def get_profile_embed(arg):
    username = urllib.parse.quote(arg.replace(' ', '+'))  #username parsing
    su = SearchUser(username)

    average_stats = su.get_average_stats()

    embed = discord.Embed(title=su.get_user_name(), url="https://www.op.gg/summoner/userName=" + username, description=su.get_top_rank(), color=0x0475b8)
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

    result_count = []
    qu_value, kda_value, type_value = '', '', ''
    type_dict = {"Normal": "일반", "Ranked": "개인/2인 랭크", "Flex": "자유 5:5 랭크",
    "Special": "특별게임모드", "ARAM": "무작위 총력전", "URF": "우르프", "Tutorial": "튜토리얼", "Bot": "봇전"}
    result_dict = {"Victory": "승", "Defeat": "패", "Remake": "무"}
    result_cnt_dict = {"Victory": 1, "Defeat": 0, "Remake": 2}

    embed = discord.Embed(title=su.get_user_name(), url="https://www.op.gg/summoner/userName=" + username, description ='개인/2인랭 자유랭크\n%s %s' %(su.get_tier()[0], su.get_tier()[1]), color=0x0475b8)
    embed.set_thumbnail(url=su.get_user_icon())
    for i in range(list_length):
        qu_value += result_dict[game_result[i]] + '\t' + game_champ[i] + '\n'    
        result_count.append(result_cnt_dict[game_result[i]]) 
        kda_value += game_KDA[i] + ' ▷' + game_rating[i] + '\n'          
        type_value += type_dict[game_types[i]] + '\n'

    embed.add_field(name=str(list_length) + '전 ', value=qu_value, inline=True)
    embed.add_field(name=str(result_count.count(1)) + '승 ' , value=kda_value, inline=True)
    embed.add_field(name=str(result_count.count(0)) + '패', value=type_value, inline=True)

    return embed