from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

class SearchUser:
    def __init__(self, username):
        url= "https://www.op.gg/summoner/userName=" + username
        html = urlopen(url)
        self.bs_obj = bs(html, 'html.parser')

    def get_user_level(self):
        profile = self.bs_obj.findAll('div', 'ProfileIcon')
        user_level = profile[0].find('span').text

        return user_level

    def get_recent_kda(self, game_count):
        kda = []

        kdas = self.bs_obj.select('div.GameItemWrap div.KDA div.KDA')
        for i in range(int(game_count)):
            game_kda = ''
            for j in range(5):
                game_kda += (''.join(kdas[i].text.split()[j]))
            kda.append(game_kda)
        return kda

    def get_recent_types(self, game_count):
        game_types = []
        game_stat = self.bs_obj.findAll('div','GameItemWrap')
        for i in range(game_count):
            game_types.append(game_stat[i].find('div', 'GameType').text.split()[0])

        return game_types

    def get_recent_result(self, game_count):
        game_results = []
        game_stat = self.bs_obj.findAll('div', 'GameItemWrap')
        for i in range(game_count):
            game_results.append(game_stat[i].find('div', 'GameResult').text.split()[0])

        return game_results

    def get_tier(self):
        summoner_solorank_tier = self.bs_obj.find('div', 'SummonerRatingMedium')
        solo_tierRank = summoner_solorank_tier.find('div', 'TierRank').text.split()
        try:
            solo_tier = solo_tierRank[0] + ' ' + solo_tierRank[1]
        except:
            solo_tier = solo_tierRank[0] + '\t'

        summoner_freerank_tier = self.bs_obj.find('div', 'sub-tier')
        free_tierRank = summoner_freerank_tier.find('div', 'sub-tier__rank-tier').text.split()
        try:
            free_tier = free_tierRank[0] + ' ' + free_tierRank[1]
        except:
            free_tier = free_tierRank[0] + '\t'

        solo_tier_img = self.bs_obj.find('div', 'SummonerRatingMedium').find('img')['src']
        free_tier_img = self.bs_obj.find('div', 'sub-tier').find('img')['src']

        return [solo_tier, free_tier, solo_tier_img, free_tier_img]

    def get_recent_rating(self, game_count):
        game_ratings = []
        game_stat = self.bs_obj.findAll('div','GameItemWrap')
        for i in range(game_count):
            game_ratings.append(game_stat[i].find('div', 'KDARatio').find('span', 'KDARatio').text)

        return game_ratings

    def get_recent_champion(self, game_count):
        champions = []
        game_stat = self.bs_obj.findAll('div','GameItemWrap')
        for i in range(game_count):
            champions.append(game_stat[i].find('div', 'ChampionName').find('a').text)
        return champions
        
    def get_average_stats(self):
        games = self.bs_obj.find('table','GameAverageStats')
        game_wl = games.find('div', 'WinRatioTitle')
        game_rate = games.find('div', 'WinRatioGraph')

        game_total = game_wl.find('span', 'total').text
        recent_win = game_wl.find('span', 'win').text
        recent_lose = game_wl.find('span', 'lose').text
        recent_rate = game_rate.find('div', "Text").text

        return [game_total, recent_win, recent_lose, recent_rate]

    def get_user_icon(self):
        profile_icon = 'https:' + self.bs_obj.find('div', 'ProfileIcon').find('img')['src']
        return profile_icon

    def get_user_name(self):
        summoner_id = self.bs_obj.find('div', 'Profile').find('span', 'Name').text
        return summoner_id

    def get_top_rank(self):
        try:
            rank = self.bs_obj.find('div', 'Profile').find('div', 'LadderRank').find('a')
        except:
            return ''
        top_rank = ''
        for i in rank.text.split():
            top_rank += i + ' '

        return top_rank.replace('Ladder Rank', '래더 랭킹').replace('(', '위 ( 상위 ').replace('of top', '')


