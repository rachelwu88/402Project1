import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!"
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

conn.close()
