import sqlite3
hewan = sqlite3.connect('database_fauna.db')

cur = hewan.cursor()
cur.execute("SELECT SUM (jumlah_skrg) FROM FAUNA")
total_fauna = cur.fetchone()[0]
print(f"TOTAL SELURUH FAUNA:{total_fauna}")

hewan.close()