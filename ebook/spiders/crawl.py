# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from ebook.items import EbookItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
import datetime
import urlparse
import socket

class CrawlSpider(SitemapSpider):
    name = 'crawl'
    sitemap_urls = []

    def parse(self, response):

        l = ItemLoader(item=EbookItem(), response=response)

        #Primary Fields
        l.add_xpath('Title', '//header/h1/text()')
        l.add_xpath('Subtitle', '//header/h4/text()')
        l.add_xpath('Image', '//img[contains(@class,"attachment-post-thumbnail")]/@src')
        # begin rework table info see nested item loaders
        l.add_xpath('Author', '')
        l.add_xpath('ISBIN', '')
        l.add_xpath('Year', '')
        l.add_xpath('Pages', '')
        l.add_xpath('Language', '')
        l.add_xpath('File_Size', '')
        l.add_xpath('File_Format', '')
        l.add_xpath('Category', '')
        #end rework table info

        #MapCompose for Description? lambda s: re.sub(r'[\n\b\f\r\t\v\x00]', ' ', s)
        l.add_xpath('Description', '//div[contains(@class,"entry-content")])
        #MapCompose replace ' ' with %20
        l.add_xpath('Download_Link', '//a[contains(@href,"file")]/@href')

        #Housekeeping Fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.now())

        return l.load_item()
