from sqlalchemy import Column, Integer, String, ForeignKey, Date

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=80), unique=True, nullable=False)
    publisher_id = Column(Integer, ForeignKey(Publisher.id), nullable=False)

    publisher = relationship(Publisher, backref='book')


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=40), unique=True, nullable=False)


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey(Book.id), nullable=False)
    shop_id = Column(Integer, ForeignKey(Shop.id), nullable=False)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    date_sale = Column(Date, nullable=False)
    stock_id = Column(Integer, ForeignKey(Stock.id), nullable=False)
    count = Column(Integer, nullable=False)

    stock = relationship(Stock, backref='sale')


def create_tables(engine):
    Base.metadata.create_all(engine)


