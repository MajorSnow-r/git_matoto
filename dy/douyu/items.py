# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    # type = scrapy.Field()
    # name = scrapy.Field()
    hn = scrapy.Field()
    url = scrapy.Field()
    pass