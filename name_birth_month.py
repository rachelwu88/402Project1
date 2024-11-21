import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ilasm28Rw!",
    database="menagerie"
)

cursor = conn.cursor()

query = "SELECT name, birth, MONTH(birth) AS `MONTH(birth)` FROM pet;"
cursor.execute(query)

results = cursor.fetchall()
print(f"{'name':<10}{'birth':<15}{'MONTH(birth)':<15}")
print("-" * 40)
for row in results:
    print(f"{row[0]:<10}{row[1]}{row[2]:>15}")

cursor.close()
conn.close()
