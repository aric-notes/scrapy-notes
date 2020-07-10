# novel site
- https://www.cnblogs.com/zhangxi1/articles/11341609.html
- http://www.xbiquge.la/xiaoshuodaquan/

## env setup
1. pip install scrapy
2. scrapy startproject 你的蜘蛛名称
3. tree:
   ```conf
    爬虫规则写在spiders目录下
    items.py ——需要爬取的数据
    pipelines.py ——执行数据保存
    settings —— 配置
    middlewares.py——下载器
    spiders
      - bookSpider.py
   ```

4. items.py
   > 这里是定义 Model ，每个详情页的 Model
   ```py
   # 2019年8月12日17:41:08
    import scrapy
    class BookspiderItem(scrapy.Item):
        # define the fields for your item here like:
        i = scrapy.Field()
        book_name = scrapy.Field()
        book_img = scrapy.Field()
        book_author = scrapy.Field()
        book_last_chapter = scrapy.Field()
        book_last_time = scrapy.Field()
        book_list_name = scrapy.Field()
        book_content = scrapy.Field()
        pass
   ```
5. 编写采集规则
```py
# 2019年8月12日17:41:08
# author zhangxi<1638844034@qq.com>
import scrapy
from ..items import BookspiderItem
class Book(scrapy.Spider):
    name = "BookSpider"
    start_urls = [
        'http://www.xbiquge.la/xiaoshuodaquan/'
    ]

    #  1. 这个是入口函数
    def parse(self, response):
        bookAllList = response.css('.novellist:first-child>ul>li')

        for all in bookAllList:
            booklist = all.css('a::attr(href)').extract_first()
            # 2. scrapy.Request( 第一个参数可以理解为 context, 第二个参数为 回调函数 )
            yield scrapy.Request(booklist,callback=self.list)

    # 3. 这里到达列表
    def list(self,response):
        book_name = response.css('#info>h1::text').extract_first()
        book_img = response.css('#fmimg>img::attr(src)').extract_first()
        book_author = response.css('#info p:nth-child(2)::text').extract_first()
        book_last_chapter = response.css('#info p:last-child::text').extract_first()
        book_last_time = response.css('#info p:nth-last-child(2)::text').extract_first()
        bookInfo = {
            'book_name':book_name,
            'book_img':book_img,
            'book_author':book_author,
            'book_last_chapter':book_last_chapter,
            'book_last_time':book_last_time
        }
        list = response.css('#list>dl>dd>a::attr(href)').extract()
        i = 0
        for var in list:
            i += 1
            bookInfo['i'] = i # 获取抓取时的顺序，保存数据时按顺序保存
            yield scrapy.Request('http://www.xbiquge.la'+var,meta=bookInfo,callback=self.info)

    def info(self,response):
        self.log(response.meta['book_name'])
        content = response.css('#content::text').extract()
        item = BookspiderItem()
        item['i'] = response.meta['i']
        item['book_name'] = response.meta['book_name']
        item['book_img'] = response.meta['book_img']
        item['book_author'] = response.meta['book_author']
        item['book_last_chapter'] = response.meta['book_last_chapter']
        item['book_last_time'] = response.meta['book_last_time']
        item['book_list_name'] = response.css('.bookname h1::text').extract_first()

        item['book_content'] = ''.join(content)
        yield item
```
