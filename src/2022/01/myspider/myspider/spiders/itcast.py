import scrapy


# logger = logging.getLogger(__name__)
# https://www.cnpython.com/qa/?page=2
# https://www.cnpython.com/qa/1472879

class ItcastSpider(scrapy.Spider):
  name = 'itcast'
  allowed_domains = ['www.cnpython.com']
  start_urls = ['https://www.cnpython.com/qa/?page=1']
  base_url = "https://www.cnpython.com"

  def parse(self, response):
    # 处理 start_urls 地址对应的响应
    list = response.css(".stream-list .stream-list__item h2.title a")
    print(len(list))
    for item in list:
      ditem = {}
      ditem["href"] = "https://www.cnpython.com" + item.xpath('.//@href').extract_first()
      ditem["title"] = item.xpath('.//text()').get()
      print("ditem:", ditem)
      yield scrapy.Request(
        ditem["href"],
        callback=self.parse_detail,
        meta={"item": ditem}
      )
    # next_url = 'https://wz.sun0769.com' + response.css('.public-content .paging-box a')[-1].xpath('.//@href').get()
    # print(next_url)
    # yield scrapy.Request(next_url, callback=self.parse)

  def parse_detail(self, response):
    item = response.meta["item"]
    item["content"] = response.css('.left-details-head .show-content').get()
    print("detial:", item)
    yield item
