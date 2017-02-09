# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#

from scrapy import Item
import scrapy

class ItJuziItem(Item):
    # name = scrapy.Field()
    invse_year = scrapy.Field()
    com_scope_id = scrapy.Field()
    com_prov = scrapy.Field()
    invse_round_id = scrapy.Field()
    cat_name = scrapy.Field()
    com_logo_archive = scrapy.Field()
    invse_month = scrapy.Field()
    invse_detail_money = scrapy.Field()
    invse_guess_particulars = scrapy.Field()
    com_id = scrapy.Field()
    current = scrapy.Field()
    invse_currency_id = scrapy.Field()
    invse_day = scrapy.Field()
    inves_round = scrapy.Field()
    com_name = scrapy.Field()
    pass

class ItJuziItemDetail(Item):
    com_id = scrapy.Field()
    invsefirm = scrapy.Field()
    com_scope_id = scrapy.Field()
    com_prov = scrapy.Field()
    com_born_year = scrapy.Field()
    tags = scrapy.Field()
    com_url = scrapy.Field()
    com_born_month = scrapy.Field()
    member = scrapy.Field()
    com_city = scrapy.Field()
    scope = scrapy.Field()
    com_des = scrapy.Field()
    
