# db config
import sqlalchemy
from dotenv import dotenv_values

config = { ** dotenv_values(".env") }

print(config)

# mysql
# engine = sqlalchemy.create_engine('mysql+pymysql://root:123456@localhost:3306/awesome_scrapy?charset=utf8mb4')