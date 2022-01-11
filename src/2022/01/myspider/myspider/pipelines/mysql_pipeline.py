# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from orator import DatabaseManager
from ..models.post import Post


class MysqlPipeline:
  def process_item(self, item, spider):
    post = Post()
    post.title = item["title"]
    post.href = item["href"]
    post.content = item["content"]
    post.save()
    return item
