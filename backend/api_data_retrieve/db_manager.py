import pymysql
from . import select_queries

HOST = "localhost"
USER = "root"
PASSWORD = ""
DB = "recipes"


class DB_Manager:
    def __init__(self, host=HOST, user=USER, pwd=PASSWORD, db=DB):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_dairy(self):
        with self.connection.cursor() as cursor:
            cursor.execute(select_queries.SELECT_DAIRY_INGREDIANTS)
            return [ingrediant["name"] for ingrediant in cursor.fetchall()]

    def get_gluten(self):
        with self.connection.cursor() as cursor:
            cursor.execute(select_queries.SELECT_GLUTEN_INGREDIANTS)
            return [ingrediant["name"] for ingrediant in cursor.fetchall()]


db_manager = DB_Manager()
