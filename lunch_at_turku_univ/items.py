# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags


class LunchItem(scrapy.Item):
    # define the fields for your item here like:
    day = scrapy.Field()
    dishes = scrapy.Field(
        input_processor=MapCompose(remove_tags),
    )
    restaurant = scrapy.Field()
