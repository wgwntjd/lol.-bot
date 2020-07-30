from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

def get_user_level(userid):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')
    
    profile = bs_obj.find('div','ProfileIcon')
    user_level = profile.find('span', 'Level tip tpd-delegation-uid-1').text

    return user_level

def get_recent_kda(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    kda = ''

    kdas = bs_obj.select('div.GameItemWrap div.KDA div.KDA')
    for i in range(int(game_count)):
        for j in range(5):
            kda += kdas[i].text.split()[j]
        kda += '\n'
    return kda

def get_recent_types(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    game_types = ''
    game_stat = bs_obj.findAll('div','GameItemWrap')
    for i in range(game_count):
        game_types += game_stat[i].find('div', 'GameType').text.split()[0] + '\n'

    return game_types

def get_recent_result(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    game_results = ''
    game_stat = bs_obj.findAll('div','GameItemWrap')
    for i in range(game_count):
        game_results += game_stat[i].find('div', 'GameResult').text.split()[0] + '\n'

    return game_results

def get_tier(userid):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    summoner_solorank_tier = bs_obj.find('div', 'SummonerRatingMedium')
    solo_tierRank = summoner_solorank_tier.find('div', 'TierRank').text
    #solo_lp = summoner_solorank_tier.find('span', 'LeaguePoints').text.replace('\t', '').replace('\n','')
    solo_tier = solo_tierRank, #solo_lp

    summoner_freerank_tier = bs_obj.find('div', 'sub-tier')
    free_tierRank = summoner_freerank_tier.find('div', 'sub-tier__rank-tier').text
    #free_lp = summoner_solorank_tier.find('div', 'sub-tier__league-point').text.replace('\t', '').replace('\n','')
    free_tier = free_tierRank, #free_lp

    return solo_tier, free_tier

def get_recent_rating(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    game_ratings = ''
    game_stat = bs_obj.findAll('div','GameItemWrap')
    for i in range(game_count):
        game_ratings += game_stat[i].find('div', 'KDARatio').find('span', 'KDARatio').text + '\n'

    return game_ratings

def get_recent_champion(userid, game_count):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    champions = ''
    game_stat = bs_obj.findAll('div','GameItemWrap')
    for i in range(game_count):
        champions += game_stat[i].find('div', 'ChampionName').find('a').text + '\n'
    return champions
    
def get_average_stats(userid):
    url = "https://www.op.gg/summoner/userName="+userid
    html = urlopen(url)
    bs_obj = bs(html, 'html.parser')

    games = bs_obj.find('table','GameAverageStats')
    game_wl = games.find('div', 'WinRatioTitle')
    game_rate = games.find('div', 'WinRatioGraph')

    game_total = game_wl.find('span', 'total').text
    recent_win = game_wl.find('span', 'win').text
    recent_lose = game_wl.find('span', 'lose').text
    recent_rate = game_rate.find('div', "Text").text

    return [game_total, recent_win, recent_lose, recent_rate]