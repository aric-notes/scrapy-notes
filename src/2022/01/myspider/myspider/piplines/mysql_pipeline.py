# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from orator import DatabaseManager
from .. import Post


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
