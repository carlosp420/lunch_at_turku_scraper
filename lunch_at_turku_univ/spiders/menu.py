# -*- coding: utf-8 -*-
import datetime

import scrapy
from lunch_at_turku_univ.items import LunchAtTurkuUnivItem as Item


class MenuSpider(scrapy.Spider):
    name = "menu"
    allowed_domains = ["unica.fi"]
    start_urls = (
        'http://www.unica.fi/en/restaurants/macciavelli/',
    )

    def parse(self, response):
        today = datetime.date.today()
        today = datetime.datetime.strftime(today, '%A')

        sel = response.xpath
        rest = sel("//title/text()").extract()
        rest = rest[0].split("|")[0].strip()

        item = Item()
        item['restaurant'] = rest

        item['dishes'] = sel("//h4[text()='" + today + "']/following-sibling::table//td[@class='lunch']/text()").extract()

        item['day'] = today

        yield item
