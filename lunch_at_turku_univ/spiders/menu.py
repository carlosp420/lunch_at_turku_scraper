# -*- coding: utf-8 -*-
import datetime

import scrapy
from lunch_at_turku_univ.items import LunchAtTurkuUnivItem as Item


class MenuSpider(scrapy.Spider):
    name = "menu"
    allowed_domains = ["unica.fi"]
    start_urls = (
        'http://www.unica.fi/en/restaurants/macciavelli/',
        'http://www.unica.fi/en/restaurants/delica/',
        'http://www.unica.fi/en/restaurants/mikro/',
        'http://www.unica.fi/en/restaurants/dental/',
        'http://www.amica.fi/en/restaurants/ravintolat-kaupungeittain/turku/turku-school-of-economics--monttu--bistro/',
    )

    def parse(self, response):
        today = datetime.date.today()
        today = datetime.datetime.strftime(today, '%A')

        sel = response.xpath
        rest = sel("//title/text()").extract()
        rest = rest[0].split("|")[0].strip()

        item = Item()

        if rest.lower() == "macciavelli":
            item['restaurant'] = rest + "-Educarium"
        elif rest.lower() == "delica":
            item['restaurant'] = rest + "-Pharmacity"
        elif rest.lower() == "mikro":
            item['restaurant'] = rest + "-Medicine"
        elif "monttu" in rest.lower():
            item['restaurant'] = "Monttu-Economics"
        else:
            item['restaurant'] = rest

        item['dishes'] = sel("//h4[text()='" + today + "']/following-sibling::table//td[@class='lunch']/text()").extract()

        item['day'] = today

        yield item
