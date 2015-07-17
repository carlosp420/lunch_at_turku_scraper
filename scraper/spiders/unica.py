# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.loader import ItemLoader

from scraper.items import LunchItem


class MenuSpider(scrapy.Spider):
    name = "unica"
    allowed_domains = ["unica.fi"]  # , "amica.fi"]
    start_urls = (
        'http://www.unica.fi/en/restaurants/macciavelli/',
        'http://www.unica.fi/en/restaurants/delica/',
        'http://www.unica.fi/en/restaurants/mikro/',
        'http://www.unica.fi/en/restaurants/dental/',
    )

    def parse(self, response):
        today = datetime.date.today()
        today_long_date = datetime.datetime.strftime(today, '%A, %d %b %Y')
        today = datetime.datetime.strftime(today, '%A')

        sel = response.xpath
        restaurant = self.get_title(sel)

        l = ItemLoader(item=LunchItem(), response=response)
        l.add_value('restaurant', restaurant)
        l.add_xpath('dishes', "//h4[text()='" + today + "']/following-sibling::table//td[@class='lunch']")
        l.add_value('day', today_long_date)

        yield l.load_item()

    def get_title(self, sel):
        rest = sel("//title/text()").extract()
        rest = rest[0].split("|")[0].strip()

        if rest.lower() == "macciavelli":
            restaurant = rest + "-Educarium"
        elif rest.lower() == "delica":
            restaurant = rest + "-Pharmacity"
        elif rest.lower() == "mikro":
            restaurant = rest + "-Medicine"
        elif "monttu" in rest.lower():
            restaurant = "Monttu-Economics"
        else:
            restaurant = rest

        return restaurant
