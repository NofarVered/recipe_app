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
        for ingredient in data_constants.dairy_ingredients:
            cursor.execute(insert_queries.INSERT_INGREDIANT,
                           [ingredient, False, True])
            CONNECTOR.commit()
        for ingredient in data_constants.gluten_ingredients:
            cursor.execute(insert_queries.INSERT_INGREDIANT,
                           [ingredient, True, False])
            CONNECTOR.commit()
