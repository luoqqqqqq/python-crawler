# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    title=scrapy.Field()
    iconurl=scrapy.Field()
    subtitle=scrapy.Field()
    contentRatingTitle=scrapy.Field()
    description= scrapy.Field()
    averageUserRating= scrapy.Field()
    images = scrapy.Field() 
        
  
    #pass
