import scrapy
from awesome_scrapy.models.site import Site


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        title = response.css('title::text').extract_first()
        entity = Site(title=title, url=response.url)
        entity.save()