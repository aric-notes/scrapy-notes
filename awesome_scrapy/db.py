import sqlalchemy
from sqlalchemy.orm import Session
from dotenv import dotenv_values

# 加载配置文件
config = dotenv_values(".env")

# 构建数据库连接字符串
db_url = f"mysql+pymysql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:3306/{config['DB_NAME']}?charset=utf8mb4"

# 创建数据库引擎
engine = sqlalchemy.create_engine(db_url)

session = Session(engine)