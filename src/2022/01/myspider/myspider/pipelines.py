# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from orator import DatabaseManager
from ...models.post import Post


class MyspiderPipeline:
  def open_spider(self, spider):
    self.file = open('items.jl', 'w')

  def close_spider(self, spider):
    self.file.close()

  def process_item(self, item, spider):
    print(item)
    line = json.dumps(item, ensure_ascii=False) + "\n"
    self.file.write(line)
    return item




class MysqlPipeline:
  def open_spider(self, spider):
    self.db = DatabaseManager(spider.settigns.get('DB_CONFIG'))

  # def close_spider(self, spider):
  # self.db.cl

  def process_item(self, item, spider):
    print(item)
    post = Post(item)
    post.save()
    return item
