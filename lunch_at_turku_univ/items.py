# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LunchItem(scrapy.Item):
    # define the fields for your item here like:
    day = scrapy.Field()
    dishes = scrapy.Field()
    restaurant = scrapy.Field()
