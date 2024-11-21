import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!",
    database="menagerie"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM pet")

for row in cursor:
    print(row)

conn.close()
