# -*- coding: utf-8 -*-
import scrapy


class ProductCrawlerSpider(scrapy.Spider):
    name = 'product_crawler'
    allowed_domains = ['alibaba.com/Products']
    start_urls = ['https://www.alibaba.com/Products']

    def parse(self, response):
        #search_keyword = response.meta["search_text"]
        parser = scrapy.Selector(response)
        products = parser.xpath("//div[@class='sub-item']")
        #iterating over search results  
        for product in products:
        #Defining the XPaths
            XPATH_PRODUCT_NAME  = ".//h4[@class='sub-title']//a/text()"
            XPATH_NUM_PRODUCT =  ".//h4[@class='sub-title']//span/text()"
            
            raw_product_name = product.xpath(XPATH_PRODUCT_NAME).extract()
            raw_num_product  = product.xpath(XPATH_NUM_PRODUCT).extract()
            
            product_name = ''.join(raw_product_name).strip() if raw_product_name else None
            num_product = ''.join(raw_num_product).strip() if raw_num_product else None
			
            yield {
            'product_name':product_name,
            'num_product':num_product
                }
