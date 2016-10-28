# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerDataItem(scrapy.Item):
    PLAYER_NAME = scrapy.Field()
    PLAYER_ID = scrapy.Field()
    SEASON_ID = scrapy.Field()
    LEAGUE_ID = scrapy.Field()
    TEAM_ID = scrapy.Field()
    TEAM_ABBREVIATION = scrapy.Field()
    PLAYER_AGE = scrapy.Field()
    GP = scrapy.Field()
    GS = scrapy.Field()
    MIN = scrapy.Field()
    FGM = scrapy.Field()
    FGA = scrapy.Field()
    FG_PCT = scrapy.Field()
    FG3M = scrapy.Field()
    FG3A = scrapy.Field()
    FG3_PCT = scrapy.Field()
    FTM = scrapy.Field()
    FTA = scrapy.Field()
    FT_PCT = scrapy.Field()
    OREB = scrapy.Field()
    DREB = scrapy.Field()
    REB = scrapy.Field()
    AST = scrapy.Field()
    STL = scrapy.Field()
    BLK = scrapy.Field()
    TOV = scrapy.Field()
    PF = scrapy.Field()
    PTS = scrapy.Field()