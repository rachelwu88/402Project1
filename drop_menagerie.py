import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!"
)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS menagerie")

conn.close()
