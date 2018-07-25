import sqlite3
conn = sqlite3.connect('15-3.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Ages")
cur.execute("CREATE TABLE Ages ( name VARCHAR(128), age INTEGER)")
cur.execute("DELETE FROM Ages")
row = cur.fetchone()
if row is None:
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Ken', 21)")
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Jan', 20)")
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Abbiegail', 16)")
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Sheafan', 25)")
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Ruo', 24)")
    cur.execute("INSERT INTO Ages (name, age) VALUES ('Airidas', 36)")
sqlstr = "SELECT hex(name || age) AS X FROM Ages ORDER BY X"
for row in cur.execute(sqlstr):
    print(row)
cur.close()
