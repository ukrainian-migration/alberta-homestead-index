# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class HomesteadsItem(Item):
    # define the fields for your item here like:
    surname = Field()
    name = Field()
    sec = Field()
    twp = Field()
    rge = Field()
    mer = Field()
    placename = Field()
    ref = Field()
    film = Field()
    file = Field()
    pass


