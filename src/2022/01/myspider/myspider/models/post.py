from orator import Model
from orator import DatabaseManager

# https://learnku.com/docs/masonite/2.3/orator-orm-orm/8297


config = {
  'mysql': {
    'driver': 'mysql',
    'host': '127.0.0.1',
    'database': 'scrapy_demo',
    'user': 'root',
    'password': '123456',
    'prefix': ''
  }
}

db = DatabaseManager(config)

Model.set_connection_resolver(db)


class Post(Model):
  pass
