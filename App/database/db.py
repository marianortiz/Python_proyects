import mysql.connector
from mysql.connector import Error
from decouple import config


def get_connection():
    try:
        return mysql.connector.connect(
            host=config('SQL_HOST'),
            port=config('SQL_PORT'),
            user=config('SQL_USER'),
            password=config('SQL_PASS'),
            db=config('SQL_DATABASE')
        )

    except Error as ex:
        raise ex
