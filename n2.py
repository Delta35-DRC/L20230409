import sqlite3

connection = sqlite3.connect('itstep_DB.sl3', 5)
cur = connection.cursor()

# print(connection)
# print(cur)

# cur.execute("CREATE TABLE first_table (name TEXT);")

# cur.execute("INSERT INTO first_table (name) VALUES ('EX1');")
# cur.execute("INSERT INTO first_table (name) VALUES ('EX2');")
# cur.execute("INSERT INTO first_table (name) VALUES ('EX3');")
# cur.execute("first_table SET 
for i in cur.execute("SELECT rowid, name FROM first_table;"):
    print(i)
connection.commit()
res = cur.fetchall()
print(res)

connection.close()
