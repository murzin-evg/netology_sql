import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from orm_models import create_tables
from personal_data import ORM_LOGIN, ORM_PASSWORD, ORM_DB_NAME
from orm_service import Service

DNS = f'postgresql+psycopg2://{ORM_LOGIN}:{ORM_PASSWORD}@localhost:5432/{ORM_DB_NAME}'
engine = sq.create_engine(DNS)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

bookstore_db = Service(session)
bookstore_db.upload_json_file('tests_data.json')
print(bookstore_db.get_publisher_books(1))
bookstore_db.get_publisher_sales(1)
print()
bookstore_db.get_publisher_sales(publisher_name="O’Reilly")
print()
bookstore_db.get_publisher_sales(publisher_name="Pearson")
print()
bookstore_db.get_publisher_sales(publisher_name="Microsoft Press")
print()
bookstore_db.get_publisher_sales(publisher_name="No starch press")
print()

bookstore_db.get_publisher_sales(2)


session.close()