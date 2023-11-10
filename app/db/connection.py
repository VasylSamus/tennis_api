import pymysql.cursors
from core.config import mysql_settings_dict


connection = pymysql.connect(**mysql_settings_dict,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connection_manticore = pymysql.Connect(
    host='127.0.0.1',
    port=9301,
    user='search_user',
    password='654321',
    database='search_db',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection_manticore.cursor()


def get_cursor_mysql_sphinx():
    return cursor
