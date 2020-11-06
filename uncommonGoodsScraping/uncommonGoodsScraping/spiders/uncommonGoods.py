import scrapy
from uncommonGoodsScraping.items import UncommongoodsscrapingItem
from uncommonGoodsScraping.items import ImgData
from scrapy.http import Request



# To read from a csv file
import csv
class UncommongoodsSpider(scrapy.Spider):
    name = 'uncommonGoods'
    allowed_domains = ['uncommongoods.com']
    start_urls = ['http://uncommongoods.com/']
# This function helps us to scrape the whole content of the website
 # by following the starting URLs in a csv file.
    def start_requests(self):
    # Read main category URLs from a csv file
        with open ("/Users/AB/Pictures/Uncommon-Goods/uncommonGoodsScraping/csvFiles/SpiderMainCategoryLinksUC.csv", "rU") as f:
            reader=csv.DictReader(f)
        for row in reader:
            url=row['url']
            link_urls = [url.format(i) for i in range(1,6)]
        for link_url in link_urls:
            print(link_url)

        request=Request(link_url, callback=self.parse_product_pages,meta={'interests': row['interests']})
        yield request
# This function scrapes the page with the help of xpath provided
    def parse_product_pages(self,response):
        item = UncommongoodsscrapingItem()
    
    # Get the HTML block where all the products are listed
    # <div> HTML element with the "product-list-item" class name
        content=response.xpath('//*[@id="frame"]/app-ug-spa/div/div/app-family-page/main/div[2]/div/ul')
    # loop through the each <div> element in the content
        for product_content in content:
            image_urls = []
    # get the product details and populate the items
            item['productId']=product_content.xpath('.//article/@id').extract_first()
            item['productName']=product_content.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "product__name", " " ))]').extract_first()
            item['price']=product_content.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "ng-lazyloaded", " " ))]/img/@src').extract_first()
            item['imageUrl']=product_content.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "price", " " ))]').extract_first()
            item['productLink']="https://www.uncommongoods.com/"+product_content.xpath('.//a/@href').extract_first()
            image_urls.append(item['imageUrl'])
            item['company']="UNCOMMON"
            item['interests']=response.meta['interests']
    
            if item['productId']==None:
                break
            yield (item)
    # download the image contained in image_urls
            yield ImgData(image_urls=image_urls)
 