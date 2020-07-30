from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

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

for i in get_average_stats('pink'):
    print(i)

