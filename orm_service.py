import json
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import or_
from orm_models import Book, Publisher, Sale, Shop, Stock


class Service:

    def __init__(self, session: Session) -> None:
        self.session = session

    def __add_commit(self, object):
        self.session.add(object)
        self.session.commit()

    def create_publisher(self, name):
        publisher = Publisher(
            name = name
        )

        self.__add_commit(publisher)

        return publisher
    
    def create_book(self, title, publisher_id):
        book = Book(
            title = title,
            publisher_id = publisher_id
        )

        self.__add_commit(book)

        return book

    def create_shop(self, name):
        shop = Shop(
            name = name
        )

        self.__add_commit(shop)

        return shop
    
    def create_stock(self, book_id, shop_id, count):
        stock = Stock(
            book_id = book_id,
            shop_id = shop_id,
            count = count
        )

        self.__add_commit(stock)

        return stock
    
    def create_sale(self, price, date_sale, stock_id, count):
        sale = Sale(
            price = price,
            date_sale = date_sale,
            stock_id = stock_id,
            count = count
        )

        self.__add_commit(sale)

        return sale
    
    def upload_json_file(self, json_path):
        with open(json_path) as jf:
            json_data = json.load(jf)

        for item in json_data:
            if item['model'] == 'publisher':
                self.create_publisher(
                    name=item['fields']['name']
                )

            if item['model'] == 'book':
                self.create_book(
                    title=item['fields']['title'],
                    publisher_id=item['fields']['id_publisher']
                )

            if item['model'] == 'shop':
                self.create_shop(
                    name=item['fields']['name']
                )

            if item['model'] == 'stock':
                self.create_stock(
                    book_id=item['fields']['id_book'],
                    shop_id=item['fields']['id_shop'],
                    count=item['fields']['count']
                )

            if item['model'] == 'sale':
                self.create_sale(
                    price=item['fields']['price'],
                    date_sale=item['fields']['date_sale'],
                    stock_id=item['fields']['id_stock'],
                    count=item['fields']['count']
                )

    def get_publisher_sales(self, publisher_id=None, publisher_name=None):
        data = self.session.query(
            Publisher.name,
            Book.title,
            Shop.name,
            Sale.price,
            Sale.date_sale
        ).join(Book).join(Stock).join(Shop).join(Sale).filter(
            or_(
            Publisher.id == publisher_id,
            Publisher.name == publisher_name
        )
        ).all()
        
        if data:
            for item in data:
                title = item[1]
                shop = item[2]
                sale = item[3]
                date = datetime.strftime(item[4], f'%d-%m-%Y')
                print(f'{title:<40} | {shop:<10} | {sale:^6} | {date:<10}')

            return data
        return

    def get_publisher_books(self, publisher_id):
        return self.session.query(Publisher.name, Book.title).join(Book).filter(Publisher.id == publisher_id).all()