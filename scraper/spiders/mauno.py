# -*- coding: utf-8 -*-
import datetime

import scrapy

from scraper.items import LunchItem


class MaunoSpider(scrapy.Spider):
    name = "mauno"
    allowed_domains = ["mauno.fi"]
    start_urls = (
        'http://www.mauno.fi/fi/keittio/lounasbuffet',
    )

    def parse(self, response):
        today = datetime.date.today()
        today_long_date = datetime.datetime.strftime(today, '%A, %d %b %Y')
        today_in_numbers = datetime.datetime.strftime(today, '%d.%m').replace('.0', '.')

        buffet = response.xpath("//p[contains(., '" + today_in_numbers + "')]/following-sibling::p[contains(., 'Lounasbuffet')]/text()").extract()

        item = LunchItem()
        item['restaurant'] = 'Mauno - Biocity'
        item['dishes'] = [buffet[0]]
        item['day'] = today_long_date

        return item
