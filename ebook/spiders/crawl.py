# -*- coding: utf-8 -*-
import scrapy


class CrawlSpider(scrapy.Spider):
    name = 'crawl'
    allowed_domains = ['sitemap']
    start_urls = ['http://sitemap/']

    def parse(self, response):
        pass
