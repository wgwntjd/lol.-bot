from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def get_recent_record(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    kills = []
    deaths = []
    assists = []
    game_types = []
    game_results = []

    game_stat = bs_obj.findAll('div','GameItemWrap')
    for i in range(int(game_count)):
        kda = game_stat[i].find('div', 'KDA')
        kills.append(kda.find('span', 'Kill').text)
        deaths.append(kda.find('span', 'Death').text)
        assists.append(kda.find('span', 'Assist').text)
        game_types.append(game_stat[i].find('div', 'GameType').text.replace('\t', '').replace('\n',''))
        game_results.append(game_stat[i].find('div', 'GameResult').text.replace('\t', '').replace('\n',''))

    return kills, deaths, assists, game_types, game_results

print(get_recent_record('IOS6', 6), sep=' ')