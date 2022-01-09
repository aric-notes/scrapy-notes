import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 处理 start_urls 地址对应的响应
        logger.warning("helo")
