import pymysql
from .constants import insert_queries
from .constants import data_constants


def load():
    CONNECTOR = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="recipes",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )

    with CONNECTOR.cursor() as cursor:
        cursor.executemany(
            insert_queries.INSERT_DAIRY_INGREDIANT, data_constants.dairy_ingredients)
        cursor.executemany(
            insert_queries.INSERT_GLUTEN_INGREDIANT, data_constants.gluten_ingredients)
        CONNECTOR.commit()
