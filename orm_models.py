import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship
import datetime as dt


Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=50), unique=True, nullable=False)

    books = relationship('Book', back_populates='publisher')

    def __str__(self) -> str:
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.id', ondelete='CASCADE'), nullable=False)
    
    publisher = relationship('Publisher', back_populates='books')
    shops = relationship('Shop', secondary='stock', back_populates='books')

    def __str__(self) -> str:
        return f'{self.id}: ({self.title}, {self.publisher_id})'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=50), unique=True, nullable=False)
    
    books = relationship('Book', secondary='stock', back_populates='shops')

    def __str__(self) -> str:
        return f'{self.id}: {self.name}'

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.id', ondelete='CASCADE'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.id', ondelete='CASCADE'), nullable=False)
    count = sq.Column(sq.SmallInteger, nullable=False)
    
    __table_args__ = (
        sq.UniqueConstraint('book_id', 'shop_id', name='UniqueConstraint_book_id_and_shop_id'),
    )

    sales = relationship('Sale', back_populates='stock')

    def __str__(self) -> str:
        return f'{self.id}: ({self.book_id}, {self.shop_id}, {self.count})'

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    price = sq.Column(sq.Float(), nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False, default=dt.datetime.now)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.id', ondelete='CASCADE'), nullable=False)
    count = sq.Column(sq.SmallInteger, nullable=False)  # погуглить проверку на то чтобы покупка в определенном магазине не превышала запасы данной книги этого магазина

    # __table_args__ = (
    #     sq.CheckConstraint('count' <= stock),
    # )

    stock = relationship('Stock', back_populates='sales')

    def __str__(self) -> str:
        return f'{self.id}: ({self.price}, {self.date_sale}, {self.stock_id}, {self.count})'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)