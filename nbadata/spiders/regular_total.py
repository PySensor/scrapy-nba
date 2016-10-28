# coding:utf-8
import scrapy
import requests
import json
from nbadata.items import PlayerDataItem


class PlayerRegularSpider(scrapy.Spider):
    name = 'regular_total'
    allowed_domains = ['nba.com']

    item = PlayerDataItem()
    player_url = "http://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=1&LeagueID=00&Season=2016-17"
    playername = []
    playeridlist = []
    player_dict = {}
    result = requests.get(player_url).text
    result = json.loads(result)
    player = result['resultSets'][0]['rowSet']
    for i in player:
        playeridlist.append(i[0])
        playername.append(i[2])
    for key, value in enumerate(playeridlist):
        player_dict[value] = playername[key]

    start_urls = [
        "http://stats.nba.com/stats/playercareerstats?LeagueID=00&PlayerID={}&PerMode=Totals".format(i)
        for i in playeridlist
                  ]

    def parse(self, response):
        contents = json.loads(response.body_as_unicode())
        content = contents['resultSets']
        for datas in content[0:1]:
            try:
                for data in datas['rowSet']:
                    item = PlayerDataItem()
                    item['PLAYER_NAME'] = PlayerRegularSpider.player_dict[data[0]]
                    item['PLAYER_ID'] = data[0]
                    item['SEASON_ID'] = data[1]
                    item['LEAGUE_ID'] = data[2]
                    item['TEAM_ID'] = data[3]
                    item['TEAM_ABBREVIATION'] = data[4]
                    item['PLAYER_AGE'] = data[5]
                    item['GP'] = data[6]
                    item['GS'] = data[7]
                    item['MIN'] = data[8]
                    item['FGM'] = data[9]
                    item['FGA'] = data[10]
                    item['FG_PCT'] = data[11]
                    item['FG3M'] = data[12]
                    item['FG3A'] = data[13]
                    item['FG3_PCT'] = data[14]
                    item['FTM'] = data[15]
                    item['FTA'] = data[16]
                    item['FT_PCT'] = data[17]
                    item['OREB'] = data[18]
                    item['DREB'] = data[19]
                    item['REB'] = data[20]
                    item['AST'] = data[21]
                    item['STL'] = data[22]
                    item['BLK'] = data[23]
                    item['TOV'] = data[24]
                    item['PF'] = data[25]
                    item['PTS'] = data[26]
                    yield item
            except:
                pass