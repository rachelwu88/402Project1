import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!",
    database="menagerie"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'F'")

for row in cursor:
    print(row)

conn.close()
