# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from .models.post import Post



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

  def process_item(self, item, spider):
    print('process item:', item)
    post = Post()
    post.title = item["title"]
    post.href = item["href"]
    post.content = item["content"]
    post.save()
    return item
