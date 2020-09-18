# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    name = scrapy.Field()
    articleUrl = scrapy.Field()
    source = scrapy.Field()
    abstracts = scrapy.Field()
    authors = scrapy.Field()
    date = scrapy.Field()
    researchAreas = scrapy.Field()
    meta = scrapy.Field()