import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!",
    database="menagerie"
)

cursor = conn.cursor()
cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")

for row in cursor:
    print(row)

conn.close()
