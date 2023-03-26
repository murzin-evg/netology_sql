from psycopg2 import sql
from DataBase import DataBase
import re


def create_tables(db: DataBase) -> (str | None):
    """
    Создание таблиц в БД.

    Функция создает таблицы client, phone_number в БД Клиенты.
    Перед созданием таблиц удаляет таблицы из БД.

    Параметры:
        db (DataBase): объект с активным подключением к БД.

    Результат:
        str | None
    """
    
    db.drop_table(
        table_name='client',
        message='Таблица client удалена.'
    )

    db.create_table(
        query="""
                CREATE TABLE IF NOT EXISTS client (
                client_id   SERIAL       PRIMARY KEY,
                name        VARCHAR(30)  NOT NULL,
                surname     VARCHAR(30)  NOT NULL,
                email       VARCHAR(50)  NOT NULL UNIQUE
                );
                """,
        message='Таблица client создана.'
    )

    db.drop_table(
        table_name='phone_number',
        message='Таблица phone_number удалена.'
    )

    db.create_table(
        query="""
                CREATE TABLE IF NOT EXISTS phone_number (
                    phone_number_id   SERIAL NOT NULL PRIMARY KEY,
                    phone_number      VARCHAR(20)  NOT NULL UNIQUE,
                    client_id         INTEGER NOT NULL REFERENCES client(client_id) ON DELETE CASCADE
                );
                """,
        message='Таблица phone_number создана.'
    )

def find_client(
        db: DataBase,
        client_id: int=None,
        name: str=None,
        surname: str=None,
        email: str=None,
        phone_number: str=None
) -> list[tuple]:
    """
    Поиск клиентов в БД.

    Осуществляет поиск клиентов в БД по заданным параметрам.
    Если параметры поиска не заданы, возвращает всех клиентов в БД.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
        name (str): имя клиента.
        surname (str): фамилия клиента.
        email (str): email клиента.
        phone_number (str): телефон клиента.
    
    Результат:
        Список клиентов в формате list[tuple].
    """

    find_client_query = """
    SELECT client_id, name, surname, email, phone_number
      FROM client
           LEFT JOIN phone_number USING(client_id)
     WHERE 
    """

    result_find_params = []
    result_params = []

    if client_id is not None:
        result_find_params.append("client_id = %s")
        result_params.append(client_id)
    
    if name is not None:
        result_find_params.append("name = %s")
        result_params.append(name)

    if surname is not None:
        result_find_params.append("surname = %s")
        result_params.append(surname)
    
    if email is not None:
        result_find_params.append("email = %s")
        result_params.append(email)

    if phone_number is not None:
        result_find_params.append("phone_number = %s")
        result_params.append(phone_number)

    if result_params:
        find_client_query += ' AND '.join(result_find_params) + ';'
    else:
        find_client_query = """
        SELECT client_id, name, surname, email, phone_number
        FROM client
            LEFT JOIN phone_number USING(client_id); 
        """

    return db.select(
        query=find_client_query,
        arg=tuple(result_params,),
        fetchone=False
    )

def __check_pattern_phone_number(phone_number: str) -> bool:
    """
    Проверяет номер телефона на соответствие шаблону.

    Параметры:
        phone_number (str): телефон клиента.

    Результат:
        bool.
    """
    pattern = r"\+?[7|8]\W?\d{3}\W?\W?\d{3}\W?\d{2}\W?\d{2}"

    if re.fullmatch(pattern=pattern, string=phone_number):
        return True
    else:
        return False
    
def __check_pattern_email(email: str) -> bool:
    """
    Проверяет email на соответствие шаблону.

    Параметры:
        email (str): email клиента.

    Результат:
        bool.
    """
    pattern = r"\w{2,19}@\w{2,6}.[a-zA-Z]{2,3}"

    if re.fullmatch(pattern=pattern, string=email):
        return True
    else:
        return False

def __check_client_data(db: DataBase, client_id: int=None, email: str=None, phone_number: str=None) -> bool:
    """
    Проверка заданных параметров на наличие в БД.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
        email (str): email клиента.
        phone_number (str): телефон клиента.
    
    Результат:
        bool.
    """

    flag = False
    if client_id:
        if find_client(db, client_id=client_id):
            flag = True
    
    if email:
        __check_pattern_email(email=email)
        if find_client(db, email=email):
            flag = True

    if phone_number:
        __check_pattern_phone_number(phone_number=phone_number)
        if find_client(db, phone_number=phone_number):
            flag = True

    return flag

def __add_client_data(db: DataBase, name: str, surname: str, email: str) -> (int | None):
    """
    Добавление клиента в таблицу client.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        name (str): имя клиента.
        surname (str): фамилия клиента.
        email (str): email клиента.
    
    Результат:
        Возвращает client_id в формате int.
    """

    if __check_client_data(db, email=email):
        print(f'Почтовый ящик {email} уже существует.')
        return

    add_client_query = """
    INSERT INTO client(name, surname, email)
        VALUES (%s, %s, %s)
    RETURNING client_id;
    """
    client_id = db.insert(
        query=add_client_query,
        arg=(name, surname, email)
    )
    print(f'Пользователь {name} {surname} создан с id {client_id[0]}.')

    return client_id[0]

def add_client_to_db(db: DataBase, name: str, surname: str, email: str, phone_number: str=None) -> (dict | None):
    """
    Добавление клиента в БД (таблицы client и phone_number).
    Если параметр phone_number не задан, то осущетсвляется добавление клиента только в таблицу client.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        name (str): имя клиента.
        surname (str): фамилия клиента.
        email (str): email клиента.
        phone_number (str): телефон клиента.
    
    Результат:
        Возвращает client_id и/или phone_number_id в формате dict.
    """
    if __check_pattern_email(email=email) is False:
        print(f'Email {email} не соответствует шаблону.')
        return
    
    result = {}

    client_id = __add_client_data(db=db, name=name, surname=surname, email=email)
    result['client_id'] = client_id
    
    if phone_number is not None:
        phone_number_id = add_phone_number(db=db, client_id=client_id, phone_number=phone_number)
        result['phone_number_id'] = phone_number_id

    return result

def add_phone_number(db: DataBase, client_id: int, phone_number: str) -> (int | None):
    """
    Добавление номера телефона клиента в БД (таблицу phone_number).

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
        phone_number (str): телефон клиента.
    
    Результат:
        Возвращает phone_number_id в формате int.
    """

    if __check_client_data(db, client_id=client_id) is not True:
        print(f'Пользователь с id {client_id} не существует.')
        return

    if __check_pattern_phone_number(phone_number=phone_number) is False:
        print(f'Номер телефона {phone_number} не соответствует шаблону.')
        return

    if __check_client_data(db, phone_number=phone_number):
        print(f'Пользователь с номером телефона {phone_number} уже существует.')
        return

    add_phone_query = """
        INSERT INTO phone_number (phone_number, client_id)
             VALUES (%s, %s)
          RETURNING phone_number_id;
        """
    phone_number_id = db.insert(
        query=add_phone_query,
        arg=(phone_number, client_id)
    )
    print(f'Телефон {phone_number} добавлен в БД и принадлежит пользователю с id {client_id}.')

    return phone_number_id[0]

def update_client(
        db:DataBase,
        client_id: int,
        name: str=None,
        surname: str=None,
        email: str= None,
        phone_number = None
) -> None:
    """
    Обновление указанных параметров клиента в БД.

        Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
        name (str): имя клиента.
        surname (str): фамилия клиента.
        email (str): email клиента.
        phone_number (str): телефон клиента.
    
    Результат:
        None.
    """
    
    if __check_client_data(db, email=email):
        print(f'Почтовый ящик {email} уже существует.')
        return 
    
    if __check_client_data(db, phone_number=phone_number):
        print(f'Пользователь с номером телефона {phone_number} уже существует.')
        return 

    dict_update_params = {
        'name': name,
        'surname': surname,
        'email': email,
        'phone_number': phone_number
    }

    for key, value in dict_update_params.items():
        if value is not None:
            update_query = """UPDATE client SET {column_name} = %(value)s WHERE client_id = %(client_id)s RETURNING *"""
            db.update(query=sql.SQL(update_query).format(column_name = sql.Identifier(key)),
                     arg={'value':value, 'client_id': client_id})
    print(f'Данные пользователя {client_id} обновлены.')
    return
    
def delete_phone_number(
        db: DataBase,
        client_id: int,
        phone_number: str
) -> (tuple | list[tuple] | None):
    """
    Удаление номера телефона клиента из таблицы phone_number.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
        phone_number (str): телефон клиента.
    
    Результат:
        Возвращает client_id, phone_number в формате tuple.
    """

    if __check_client_data(db, client_id=client_id, phone_number=phone_number) is not True:
        print(f'Пользователя с номером телефона {phone_number} не существует.')
        return

    delete_phone_number_query = """
    DELETE FROM phone_number
          WHERE client_id = %s
                AND phone_number = %s
      RETURNING (client_id, phone_number);
    """

    return db.delete(
        query=delete_phone_number_query,
        arg=(client_id, phone_number),
        fetchone=True
    )

def delete_client(db: DataBase, client_id: int) -> (tuple | list[tuple] |None):
    """
    Удаление клиента из БД.

    Параметры:
        db (DataBase): объект с активным подключением к БД.
        client_id (int): id клиента в таблице client.
    
    Результат:
        Возвращает client_id в формате tuple.
    """

    if __check_client_data(db, client_id=client_id) is not True:
        print(f'Пользователь с id {client_id} не существует.')
        return

    delete_client_query = """
    DELETE FROM client
          WHERE client_id = %s
      RETURNING client_id;
    """

    return db.delete(query=delete_client_query, arg=(client_id,), fetchone=True)
    
#===============================================================================================================

if __name__ == '__main__':

    client_db = DataBase('client_db')

    create_tables(db=client_db)  # создание таблиц в БД

    # добавление клиента
    add_client_to_db(db=client_db, name='Александр', surname='Овечкин', email='alexovechkin8@wc.com', phone_number='+7(917) 888-88-88')
    add_client_to_db(db=client_db, name='Конор', surname='Макдэвид', email='conormcdavid@ya.ru')
    add_client_to_db(db=client_db, name='Артемий', surname='Панарин', email='panarin10@nyr.com', phone_number='+7(910) 100-10-10')
    add_client_to_db(db=client_db, name='Вася', surname='Кошечкин', email='vasya@ya.ru')
    add_client_to_db(db=client_db, name='Нонна', surname='Васильева', email='nonna@ya.ru', phone_number='5 917 345-66-87')
    add_client_to_db(db=client_db, name='Галечка', surname='Петрова', email='gaaaaalya@yaru')

    # поиск клиента
    print(find_client(db=client_db, name='Александр'))
    print(find_client(db=client_db, surname='Овечкин'))
    print(find_client(db=client_db, phone_number='+7(917) 888-88-88'))
    print(find_client(db=client_db, email='alexovechkin8@wc.com'))
    print()
    print(find_client(db=client_db, name='Александр', surname='Макдэвид'))
    print(find_client(db=client_db, name='Конор', surname='Макдэвид'))
    print(find_client(db=client_db, name='Конор'))
    print(find_client(db=client_db, surname='Макдэвид'))
    print(find_client(db=client_db, email='conormcdavid@ya.ru'))
    print()
    print(find_client(db=client_db, name='Артемий', phone_number='+7(910) 100-10-10'))
    print(find_client(db=client_db, surname='Панарин'))
    print(find_client(db=client_db, email='panarin10@nyr.com'))
    print(find_client(db=client_db, phone_number='+7(910) 100-10-10'))
    print()
    print(find_client(db=client_db))
    print()
    print(find_client(db=client_db, client_id=4))

    # добавление номера
    # add_phone_number(db=client_db, client_id=3, phone_number='+7(917) 454-75-88')
    # add_phone_number(db=client_db, client_id=2, phone_number='+7(917) 222-73-44')
    # print(find_client(db=client_db))
    # print()

    # обновление данных
    update_client(db=client_db, client_id=4, name='Герман', surname='Жуков')
    update_client(db=client_db, client_id=4, name='Вася')
    print(find_client(db=client_db))
    print()

    # удаление телефона у существующего клиента
    # delete_phone_number(db=client_db, client_id=3, phone_number='+7(910) 100-10-10')
    # delete_phone_number(db=client_db, client_id=5, phone_number='+7(910) 100-10-10')
    # print(find_client(db=client_db))
    # print()

    # удаление клиента
    # delete_client(db=client_db, client_id=5)
    # delete_client(db=client_db, client_id=4)
    # print(find_client(db=client_db))
    # print()

    client_db.close()




