import scrapy
import json
from uncommonGoodsScraping.items import UncommongoodsscrapingItem





# To read from a csv file
import csv
class UncommongoodsSpider(scrapy.Spider):
    name = 'uncommonGoods'
    allowed_domains = ['uncommongoods.com']
    start_urls = ['https://www.uncommongoods.com/br/search/?account_id=5343&auth_key=&domain_key=uncommongoods&request_type=search&br_origin=searchBox&search_type=category&fl=pid%2Ctitle%2Cprice%2Cthumb_image%2Cthumb_image_alt%2Curl%2Creviews%2Creviews_count%2Cprice_range%2Cbr_min_sale_price%2Cbr_max_sale_price%2Cugoods_sale_price%2Cdays_live%2Cmin_inventory%2Cis_customizable%2Cnum_skus%2Cis_coming_soon%2Cvideo_link%2Cmin_age%2Cmax_age%2Cis_ship_delay%2Cavailability_attr%2Cavailable_inventory%2Ctop_review_headline%2Ctop_review_comment%2Cshow_only_on_sale_page&efq=-show_only_on_sale_page:%221%22&request_id=953690550831.1255&facet.field=ug_cat_internal&facet.field=recipients&_br_uid_2=uid=1627670274406:v=12.0:ts=1603493123208:hc=17&q=funbyinterestsportsgifts&rows=120&start=0&custom_country=US&url=%22%2Ffun%2Fby-interest%2Fsports-gifts%26custom_country%3D%22US&ref_url=%22%2Ffun%2Fby-interest%2Fsports-gifts%22']

    def parse(self, response):
        item = UncommongoodsscrapingItem()
        data = json.loads(response.body)
        for product in data["docs"]:
            item['productName'] = product['title']
            yield(item)
        
'http://www.uncommongoods.com/br/search/?account_id=5343&auth_key=&domain_key=uncommongoods&request_type=search&br_origin=searchBox&search_type=category&fl=pid%2Ctitle%2Cprice%2Cthumb_image%2Cthumb_image_alt%2Curl%2Creviews%2Creviews_count%2Cprice_range%2Cbr_min_sale_price%2Cbr_max_sale_price%2Cugoods_sale_price%2Cdays_live%2Cmin_inventory%2Cis_customizable%2Cnum_skus%2Cis_coming_soon%2Cvideo_link%2Cmin_age%2Cmax_age%2Cis_ship_delay%2Cavailability_attr%2Cavailable_inventory%2Ctop_review_headline%2Ctop_review_comment%2Cshow_only_on_sale_page&efq=-show_only_on_sale_page:%221%22&request_id=953690550831.1255&facet.field=ug_cat_internal&facet.field=recipients&_br_uid_2=uid=1627670274406:v=12.0:ts=1603493123208:hc=17&q=funbyinterestsportsgifts&rows=120&start=0&custom_country=US&url=%22%2Ffun%2Fby-interest%2Fsports-gifts%26custom_country%3D%22US&ref_url=%22%2Ffun%2Fby-interest%2Fsports-gifts%22'