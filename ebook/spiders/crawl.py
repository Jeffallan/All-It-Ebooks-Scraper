# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from ebook.items import EbookItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from datetime import date
# import urlparse
import socket

class CrawlSpider(SitemapSpider):
    name = 'map'
    sitemap_urls = ['http://www.allitebooks.com/post-sitemap1.xml',
                    'http://www.allitebooks.com/post-sitemap2.xml',
                    'http://www.allitebooks.com/post-sitemap3.xml',
                    'http://www.allitebooks.com/post-sitemap4.xml',
                    'http://www.allitebooks.com/post-sitemap5.xml',
                    'http://www.allitebooks.com/post-sitemap6.xml',
                    'http://www.allitebooks.com/post-sitemap7.xml',
                    'http://www.allitebooks.com/post-sitemap8.xml']
    # sitemap_follow = ['/post_sitemap1.xml']

    def parse(self, response):

        l = ItemLoader(item=EbookItem(), response=response)

        # Primary Fields
        l.add_xpath('Title', '//header/h1/text()', MapCompose(unicode.strip))
        l.add_xpath('Subtitle', '//header/h4/text()', MapCompose(unicode.strip))
        l.add_xpath('Image', '//img[contains(@class,"attachment-post-thumbnail")]/@src',
                    MapCompose(unicode.strip))
        l.add_xpath('Author', '//div[contains(@class, "book-detail")]//dd[1]/a/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('ISBIN', '//div[contains(@class, "book-detail")]//dd[2]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('Year', '//div[contains(@class, "book-detail")]//dd[3]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('Pages', '//div[contains(@class, "book-detail")]//dd[4]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('Language', '//div[contains(@class, "book-detail")]//dd[5]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('File_Size', '//div[contains(@class, "book-detail")]//dd[6]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('File_Format', '//div[contains(@class, "book-detail")]//dd[7]/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('Category', '//div[contains(@class, "book-detail")]//dd[8]//a/text()',
                    MapCompose(unicode.strip))
        l.add_xpath('Description', '//div[contains(@class,"entry-content")]',
                    MapCompose(lambda s: s.replace('\n', ''),
                               lambda s: s.replace('\b', ''),
                               lambda s: s.replace('\f', ''),
                               lambda s: s.replace('\r', ''),
                               lambda s: s.replace('\t', ''),
                               lambda s: s.replace('\v', ''),
                               lambda s: s.replace('\x00', ''),
                               unicode.strip))
        l.add_xpath('Download_Link', '//a[contains(@href,"file")]/@href',
                    MapCompose(lambda s: s.replace(' ', '%20'), unicode.strip))

        # Housekeeping Fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        # l.add_value('date', date.today())

        return l.load_item()
