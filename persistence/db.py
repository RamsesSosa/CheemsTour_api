import mysql.connector 
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="",
        user="",
        password="",
        database=""
    )
    