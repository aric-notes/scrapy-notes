from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Site(DeclarativeBase):
    __tablename__ = "sites"
    id = mapped_column(ForeignKey("address.id"), primary_key=True)
    title = mapped_column(String(50))
    url = mapped_column(String(100))

    is_crawled = mapped_column(Integer, default=0)
    created_at = mapped_column(DateTime, nullable=False, default=DateTime.now)
    updated_at = mapped_column(DateTime, nullable=False, default=DateTime.now, onupdate=DateTime.now)
