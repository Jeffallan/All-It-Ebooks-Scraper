# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class EbookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Primary Fields
    Title = Field()
    Subtitle = Field()
    Image = Field()
    Author = Field()
    ISBIN-10 = Field()
    Year = Field()
    Pages = Field()
    Language = Field()
    File Size = Field()
    File Format = Field()
    Category = Field()
    Description = Field()
    Download_Link = Field()

    # Hosekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
