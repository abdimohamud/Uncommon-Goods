# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#items.py in fashionWebScraping folder
import scrapy
from scrapy.item import Item, Field
class UncommongoodsscrapingItem(scrapy.Item):
 
 #product related items, such as id,name,price
    productName=Field()
 
