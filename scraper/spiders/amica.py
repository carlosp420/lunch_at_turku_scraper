# -*- coding: utf-8 -*-
import scrapy


class AmicaSpider(scrapy.Spider):
    name = "amica"
    allowed_domains = ["amica.fi"]
    start_urls = (
        'http://www.amica.fi/en/restaurants/ravintolat-kaupungeittain/turku/turku-school-of-economics--monttu--bistro/',

    )

    def parse(self, response):
        """Monttu is closed during the summer"""
        pass
