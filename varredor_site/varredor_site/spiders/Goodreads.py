import scrapy
import scrapy
from scrapy.loader import ItemLoader
from varredor_site.items import CitacaoItem



# CanekCase


class GoodReadsSpider(scrapy.Spider):
    #Identidade
    name = 'quotebot'
   
    #Request
    def start_requests(self):
        # Definir url(s) a varrer
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    #Response
    def parse(self, response):
        # aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(), selector=elemento, response=response)
            loader.add_xpath('frase',".//div[@class='quoteText']/text()" )
            loader.add_xpath('autor',".//span[@class='authorOrTitle']/text()" )
            loader.add_xpath('tags',".//div[@class='greyText smallText left']/a/text()" )
            yield loader.load_item()
            
