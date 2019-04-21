import scrapy

#inheriting from  scrapy object spider - can directly use property
class  QuoteSpider(scrapy.Spider):
    name = 'quotes'
#Provide list of URL's to scrap
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

#def method , refer to class itself self,
#response - contain source code of website. extract title, tag perticular which you want.
    def parse(self,response):
        title = response.css('title::text').extract()
#yield - can say it work as return keyword. USed with generator use by scrapy behind the scene
        yield {'titletext' : title}
