# -*- coding: utf-8 -*-
import json
import codecs
from twisted.enterprise import adbapi
import pymysql

pymysql.install_as_MySQLdb()


class MySQLStorePipelines(object):
    def __init__(self):
        dbargs = dict(
            host='127.0.0.1',
            db='nba_player',
            user='root',
            passwd='3582100',
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8',
            use_unicode=True
        )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    def process_item(self, item, spider):
        if spider.name == 'regular':
            res = self.dbpool.runInteraction(self.regular_data, item)
            return item
        if spider.name == 'regular_total':
            res = self.dbpool.runInteraction(self.regular_total_data, item)
            return item
        elif spider.name == 'playoff':
            res = self.dbpool.runInteraction(self.playoff_data, item)
            return item
        elif spider.name == 'playoff_total':
            res = self.dbpool.runInteraction(self.playoff_total_data, item)
            return item
        elif spider.name == 'allstar':
            res = self.dbpool.runInteraction(self.allstar_data, item)
            return item
        elif spider.name == 'university':
            res = self.dbpool.runInteraction(self.university_data, item)
            return item
        elif spider.name == 'player':
            res = self.dbpool.runInteraction(self.player_data, item)
            return item
        elif spider.name == 'player_total':
            res = self.dbpool.runInteraction(self.player_total_data, item)
            return item

    def regular_data(self, conn, item):
        conn.execute('''insert into regular(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                    TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                    FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                    TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                        item['PLAYER_NAME'],
                        item['PLAYER_ID'],
                        item['SEASON_ID'],
                        item['LEAGUE_ID'],
                        item['TEAM_ID'],
                        item['TEAM_ABBREVIATION'],
                        item['PLAYER_AGE'],
                        item['GP'],
                        item['GS'],
                        item['MIN'],
                        item['FGM'],
                        item['FGA'],
                        item['FG_PCT'],
                        item['FG3M'],
                        item['FG3A'],
                        item['FG3_PCT'],
                        item['FTM'],
                        item['FTA'],
                        item['FT_PCT'],
                        item['OREB'],
                        item['DREB'],
                        item['REB'],
                        item['AST'],
                        item['STL'],
                        item['BLK'],
                        item['TOV'],
                        item['PF'],
                        item['PTS']))

    def regular_total_data(self, conn, item):
        conn.execute('''insert into regular_total(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                    TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                    FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                    TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
            item['PLAYER_NAME'],
            item['PLAYER_ID'],
            item['SEASON_ID'],
            item['LEAGUE_ID'],
            item['TEAM_ID'],
            item['TEAM_ABBREVIATION'],
            item['PLAYER_AGE'],
            item['GP'],
            item['GS'],
            item['MIN'],
            item['FGM'],
            item['FGA'],
            item['FG_PCT'],
            item['FG3M'],
            item['FG3A'],
            item['FG3_PCT'],
            item['FTM'],
            item['FTA'],
            item['FT_PCT'],
            item['OREB'],
            item['DREB'],
            item['REB'],
            item['AST'],
            item['STL'],
            item['BLK'],
            item['TOV'],
            item['PF'],
            item['PTS']))

    def playoff_data(self, conn, item):
            conn.execute('''insert into playoff(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                        TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                        FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                        TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                item['PLAYER_NAME'],
                item['PLAYER_ID'],
                item['SEASON_ID'],
                item['LEAGUE_ID'],
                item['TEAM_ID'],
                item['TEAM_ABBREVIATION'],
                item['PLAYER_AGE'],
                item['GP'],
                item['GS'],
                item['MIN'],
                item['FGM'],
                item['FGA'],
                item['FG_PCT'],
                item['FG3M'],
                item['FG3A'],
                item['FG3_PCT'],
                item['FTM'],
                item['FTA'],
                item['FT_PCT'],
                item['OREB'],
                item['DREB'],
                item['REB'],
                item['AST'],
                item['STL'],
                item['BLK'],
                item['TOV'],
                item['PF'],
                item['PTS']))

    def playoff_total_data(self, conn, item):
            conn.execute('''insert into playoff_total(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                        TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                        FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                        TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                item['PLAYER_NAME'],
                item['PLAYER_ID'],
                item['SEASON_ID'],
                item['LEAGUE_ID'],
                item['TEAM_ID'],
                item['TEAM_ABBREVIATION'],
                item['PLAYER_AGE'],
                item['GP'],
                item['GS'],
                item['MIN'],
                item['FGM'],
                item['FGA'],
                item['FG_PCT'],
                item['FG3M'],
                item['FG3A'],
                item['FG3_PCT'],
                item['FTM'],
                item['FTA'],
                item['FT_PCT'],
                item['OREB'],
                item['DREB'],
                item['REB'],
                item['AST'],
                item['STL'],
                item['BLK'],
                item['TOV'],
                item['PF'],
                item['PTS']))

    def allstar_data(self, conn, item):
            conn.execute('''insert into allstar(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                        TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                        FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                        TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                item['PLAYER_NAME'],
                item['PLAYER_ID'],
                item['SEASON_ID'],
                item['LEAGUE_ID'],
                item['TEAM_ID'],
                item['TEAM_ABBREVIATION'],
                item['PLAYER_AGE'],
                item['GP'],
                item['GS'],
                item['MIN'],
                item['FGM'],
                item['FGA'],
                item['FG_PCT'],
                item['FG3M'],
                item['FG3A'],
                item['FG3_PCT'],
                item['FTM'],
                item['FTA'],
                item['FT_PCT'],
                item['OREB'],
                item['DREB'],
                item['REB'],
                item['AST'],
                item['STL'],
                item['BLK'],
                item['TOV'],
                item['PF'],
                item['PTS']))

    def university_data(self, conn, item):
            conn.execute('''insert into university_data(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                        TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                        FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                        TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                item['PLAYER_NAME'],
                item['PLAYER_ID'],
                item['SEASON_ID'],
                item['LEAGUE_ID'],
                item['TEAM_ID'],
                item['TEAM_ABBREVIATION'],
                item['PLAYER_AGE'],
                item['GP'],
                item['GS'],
                item['MIN'],
                item['FGM'],
                item['FGA'],
                item['FG_PCT'],
                item['FG3M'],
                item['FG3A'],
                item['FG3_PCT'],
                item['FTM'],
                item['FTA'],
                item['FT_PCT'],
                item['OREB'],
                item['DREB'],
                item['REB'],
                item['AST'],
                item['STL'],
                item['BLK'],
                item['TOV'],
                item['PF'],
                item['PTS']))

    def player_data(self, conn, item):
        conn.execute('''insert into player_data(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                    TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                    FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                    TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                        item['PLAYER_NAME'],
                        item['PLAYER_ID'],
                        item['SEASON_ID'],
                        item['LEAGUE_ID'],
                        item['TEAM_ID'],
                        item['TEAM_ABBREVIATION'],
                        item['PLAYER_AGE'],
                        item['GP'],
                        item['GS'],
                        item['MIN'],
                        item['FGM'],
                        item['FGA'],
                        item['FG_PCT'],
                        item['FG3M'],
                        item['FG3A'],
                        item['FG3_PCT'],
                        item['FTM'],
                        item['FTA'],
                        item['FT_PCT'],
                        item['OREB'],
                        item['DREB'],
                        item['REB'],
                        item['AST'],
                        item['STL'],
                        item['BLK'],
                        item['TOV'],
                        item['PF'],
                        item['PTS']))

    def player_total_data(self, conn, item):
        conn.execute('''insert into player_total(PLAYER_NAME, PLAYER_ID, SEASON_ID, LEAGUE_ID,
                    TEAM_ID, TEAM_ABBREVIATION, PLAYER_AGE, GP, GS, MIN, FGM, FGA, FG_PCT,
                    FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB, REB, AST, STL, BLK,
                    TOV, PF, PTS)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                        item['PLAYER_NAME'],
                        item['PLAYER_ID'],
                        item['SEASON_ID'],
                        item['LEAGUE_ID'],
                        item['TEAM_ID'],
                        item['TEAM_ABBREVIATION'],
                        item['PLAYER_AGE'],
                        item['GP'],
                        item['GS'],
                        item['MIN'],
                        item['FGM'],
                        item['FGA'],
                        item['FG_PCT'],
                        item['FG3M'],
                        item['FG3A'],
                        item['FG3_PCT'],
                        item['FTM'],
                        item['FTA'],
                        item['FT_PCT'],
                        item['OREB'],
                        item['DREB'],
                        item['REB'],
                        item['AST'],
                        item['STL'],
                        item['BLK'],
                        item['TOV'],
                        item['PF'],
                        item['PTS']))