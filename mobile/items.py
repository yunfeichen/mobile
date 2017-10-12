# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MobileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    quhao = scrapy.Field()
    operator = scrapy.Field()
    brand = scrapy.Field()
    pass
