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
    sitemap_urls = ['http://www.allitebooks.com/sitemap_index.xml']

    def parse(self, response):

        l = ItemLoader(item=EbookItem(), response=response)

        # Primary Fields
        l.add_xpath('Title', '//header/h1/text()')
        l.add_xpath('Subtitle', '//header/h4/text()')
        l.add_xpath('Image', '//img[contains(@class,"attachment-post-thumbnail")]/@src')
        # begin rework table info see nested item loaders
        l.add_xpath('Author', '//div[contains(@class, "book-detail")]//dd[1]/a/text()')
        l.add_xpath('ISBIN', '//div[contains(@class, "book-detail")]//dd[2]/text()')
        l.add_xpath('Year', '//div[contains(@class, "book-detail")]//dd[3]/text()')
        l.add_xpath('Pages', '//div[contains(@class, "book-detail")]//dd[4]/text()')
        l.add_xpath('Language', '//div[contains(@class, "book-detail")]//dd[5]/text()')
        l.add_xpath('File_Size', '//div[contains(@class, "book-detail")]//dd[6]/text()')
        l.add_xpath('File_Format', '//div[contains(@class, "book-detail")]//dd[7]/text()')
        l.add_xpath('Category', '//div[contains(@class, "book-detail")]//dd[8]/text()')
        # end rework table info

        # MapCompose for Description? lambda s: re.sub(r'[\n\b\f\r\t\v\x00]', ' ', s)
        l.add_xpath('Description', '//div[contains(@class,"entry-content")]',
                    MapCompose(lambda s: re.sub(r'[\n\b\f\r\t\v\x00]', '', s)))
        # MapCompose replace ' ' with %20
        l.add_xpath('Download_Link', '//a[contains(@href,"file")]/@href',
                    MapCompose(lambda i: i.replace(' ', '%20')))

        # Housekeeping Fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.now())

        return l.load_item()
