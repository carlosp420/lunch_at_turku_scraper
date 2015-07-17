# -*- coding: utf-8 -*-
import scrapy


class CafeArkenSpider(scrapy.Spider):
    name = "cafe_arken"
    allowed_domains = ["studentlunch.fi"]
    start_urls = (
        'http://www.studentlunch.fi/',
    )

    def parse(self, response):
        pass
