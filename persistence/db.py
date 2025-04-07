import mysql.connector 
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="ls-ef4300d410ebc1a8304030b638b03ed2da87f5c1.c90u2ss6wl6d.us-east-2.rds.amazonaws.com",
        user="dbmasteruser",
        password="SicnoLab2025",
        database="CheemsTour"
    )