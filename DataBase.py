import psycopg2
from psycopg2 import sql

class DataBase:
    """
    Управление Базой Данных PostgreSQL.
    """

    def __init__(self, db_name: str) -> None:
        
        with open(file=f'{db_name}_login.txt', mode='r', encoding='utf-8') as file:
            login = file.read().strip()

        with open(file=f'{db_name}_password.txt', mode='r', encoding='utf-8') as file:
            __password__ = file.read().strip()

        self.connection = psycopg2.connect(
            database=db_name,
            user=login,
            password=__password__
            )
        
        self.connection.autocommit = True

    def __execute(self, cursor, query: str, arg: tuple=None) -> None:
        """
        Выполняет SQL-запрос.

        Параметры:
            cursor (psycopg2.connect.cursor()): активный курсор.
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
        
        Результат:
            Возвращает None.
        """
        
        if arg:
            cursor.execute(query, arg)
        else:
            cursor.execute(query)

    def __error(self, error):
        """
        Обрабатывает ситуации:
            1. ответ не содержит данных (ошибка)

        Параметры:
            error: ответ не содержит данных или ошибка БД.
        """
        print(error)

        return None

    def fetch_one(self, query: str, arg: tuple=None) -> (tuple | None):
        """
        Возвращает одно единственное значение в объекте типа tuple.

        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
        
        Результат:
            Возвращает одно единственное значение в объекте типа tuple.
        
        Возможные ошибки:
            - ошибка БД;
            - нет данных.

            Ошибки обрабатываются с помощью конструкции try-except.

            При ошибке метод вернет None.
        """

        try:
            cur = self.connection.cursor()
            self.__execute(cursor=cur, query=query, arg=arg)

            return cur.fetchone()
        
        except (Exception, psycopg2.Error) as error:
            self.__error(error)

    def fetch_all(self, query: str, arg: tuple=None) -> (list[tuple] | None):
        """
        Возвращает все данные соответствующие запросу в объекте типа list[tuple].

        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
        
        Результат:
            Возвращает все данные соответствующие запросу в объекте типа list[tuple].
        
        Возможные ошибки:
            - ошибка БД;
            - нет данных.

            Ошибки обрабатываются с помощью конструкции try-except.

            При ошибке метод вернет None.
        """

        try:
            cur = self.connection.cursor()
            self.__execute(cursor=cur, query=query, arg=arg)

            return cur.fetchall()
        
        except (Exception, psycopg2.Error) as error:
            self.__error(error)

    def close(self) -> None:
        """
        Закрывает активное соединение курсора и активное соединение БД.
        """

        cur = self.connection.cursor()
        cur.close()
        self.connection.close()

    def drop_table(self, table_name: str, message: str=None) -> (str | None):
        """
        Удаление таблицы из БД.
        
        Метод удаляет таблицу из БД и возвращает сообщение об успешной операции.

        Параметры:
            table_name (str): название таблицы в БД.
            message (str): сообщение об успешной операции.

        Результат:
            str | None
        """

        try:
            cur = self.connection.cursor()
            
            drop_query = "DROP TABLE IF EXISTS {} CASCADE;"

            cur.execute(
                query=sql.SQL(drop_query).format(sql.Identifier(table_name))
            )
            print(message)
            
        except (Exception, psycopg2.Error) as error:
            self.__error(error)
    
    def create_table(self, query: str, message: str=None) -> (str | None):
        """
        Создание таблицы в БД.

        Метод создает таблицу с параметрами, указанными в SQL-запросе и возвращает сообщение об успешной операции.
        
        Параметры:
            query (str) : SQL-запрос.
            message (str): сообщение об успешной операции.

        Результат:
            str | None
        """

        try:
            cur = self.connection.cursor()

            cur.execute(
                query=query
            )
            print(message)
        
        except (Exception, psycopg2.Error) as error:
            self.__error(error)
    
    def insert(self, query: str, arg: tuple=None) -> (tuple | None):
        """
        Добавление данных в таблицы БД.

        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
        
        Результат:
            tuple | None

            Для возврата результата в SQL-запросе
            необходимо прописать инструкцию RETURNING *, где:
                1) * - вернет всю строчку с данными;
                2) вместо "*" можно прописать требуемые поля для возврата.
        """
        return self.fetch_one(
            query=query,
            arg=arg
        )
        
    def select(self, query: str, arg: tuple=None, fetchone=True) -> (tuple | list[tuple] |None):
        """
        Чтение данных из таблиц БД.
        
        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
            fetchone (bool): True - возвращает одно единственное значение.
                             False - возвращает все данные соответствующие запросу.
        
        Результат:
            tuple | list[tuple] |None
        """

        if fetchone:
            return self.fetch_one(
                query=query,
                arg=arg
            )
        else:
            return self.fetch_all(
                query=query,
                arg=arg
            )

    def delete(self, query: str, arg: tuple=None, fetchone=True) -> (tuple | list[tuple] |None):
        """
        Удаление данных из БД.

        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
            fetchone (bool): True - возвращает одно единственное значение.
                             False - возвращает все данные соответствующие запросу.

        Результат:
            tuple | list[tuple] |None

            Для возврата результата в SQL-запросе
            необходимо прописать инструкцию RETURNING *, где:
                1) * - вернет всю строчку с данными;
                2) вместо "*" можно прописать требуемые поля для возврата.
        """

        if fetchone:
            return self.fetch_one(
                query=query,
                arg=arg
            )
        else:
            return self.fetch_all(
                query=query,
                arg=arg
            )

    def update(self, query: str, arg: tuple=None, fetchone=True) -> (tuple | list[tuple] |None):
        """
        Обновление данных в БД.

        Параметры:
            query (str): SQL-запрос.
            arg (tuple): аргументы для метода execute с целью подстановки в SQL-запрос.
            fetchone (bool): True - возвращает одно единственное значение.
                             False - возвращает все данные соответствующие запросу.

        Результат:
            tuple | list[tuple] |None

            Для возврата результата в SQL-запросе
            необходимо прописать инструкцию RETURNING *, где:
                1) * - вернет всю строчку с данными;
                2) вместо "*" можно прописать требуемые поля для возврата.
        """

        if fetchone:
            return self.fetch_one(
                query=query,
                arg=arg
            )
        else:
            return self.fetch_all(
                query=query,
                arg=arg
            )
    