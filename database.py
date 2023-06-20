import mysql.connector as mysql
mysql.connect(host="host", user="username", password="password", database="database")
from typing import Union
from .user import User


class Database:
    import mysql.connector
    from typing import Union
    from .user import User


    class Database:
        def __init__(self, host: str, username: str, password: str, database: str):
            self.connection = mysql.connector.connect(
                host=host,
                user=username,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()

        def add_user(self, user: User) -> None:
            query = "INSERT INTO users (username, score, total_score) VALUES (%s, %s, %s)"
            values = (user.username, user.score, user.total_score)
            self.cursor.execute(query, values)
            self.connection.commit()

        def get_user(self, username: str) -> Union[User, None]:
            query = "SELECT * FROM users WHERE username = %s"
            values = (username,)
            self.cursor.execute(query, values)
            result = self.cursor.fetchone()
            if result:
                return User(*result)
            else:
                return None

    def add_user(self, user: User) -> None:
        query = "INSERT INTO users (username, score, total_score) VALUES (%s, %s, %s)"
        values = (user.username, user.score, user.total_score)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_user(self, username: str) -> Union[User, None]:
        query = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return User(*result)
        else:
            return None
