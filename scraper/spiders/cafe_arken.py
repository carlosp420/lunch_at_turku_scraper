# -*- coding: utf-8 -*-
import datetime

import scrapy
from scrapy.loader import ItemLoader

from scraper.items import LunchItem


class CafeArkenSpider(scrapy.Spider):
    name = "cafe_arken"
    allowed_domains = ["studentlunch.fi"]

    def start_requests(self):
        # http://www.studentlunch.fi/en/lunch-list/weeks-list?id=1&year=2015&week=29
        url = 'http://www.studentlunch.fi/en/lunch-list/weeks-list'
        this_year, this_week = get_year_week()
        cafe_arken_url = '{}?id=1&year={}&week={}'.format(url, this_year, this_week)
        return [scrapy.Request(cafe_arken_url)]

    def parse(self, response):
        today = datetime.date.today()
        today_long_date = datetime.date.strftime(today, '%A, %d %b %Y')
        todays_date = construct_todays_date().lower()

        dishes = []
        for i in response.xpath('//h3'):
            if todays_date in i.extract():
                table = i.xpath('following-sibling::table')[0]
                for j in table.xpath('.//td/a/text()'):
                    dishes.append(j.extract().strip())
                break


        l = ItemLoader(item=LunchItem(), response=response)
        l.add_value('restaurant', u'Café ARKEN')
        l.add_value('day', today_long_date)
        l.add_value('dishes', dishes)
        yield l.load_item()


def get_year_week():
    date_as_iso = datetime.date.today().isocalendar()
    return date_as_iso[0], date_as_iso[1]


def construct_todays_date():
    x = datetime.date.today()
    return datetime.date.strftime(x, '%A %d.%m.%Y')
