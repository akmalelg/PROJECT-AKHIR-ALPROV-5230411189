import sqlite3
hewan = sqlite3.connect('database_fauna.db')

cur = hewan.cursor()
cur.execute("SELECT* FROM FAUNA WHERE JENIS = 'mamalia'")
baris_tabel = cur.fetchall()

print("DATA HEWAN MAMALIA JAMAN SEKARANG 2023")
print('-'*130)
print("{:<15}{:<25}{:<25}{:<25}{:<25}".format("ID FAUNA", "JENIS", "ASAL", "JUMLAH SEKARANG", "TAHUN DI TEMUKAN"))
print('-'*130)

for baris in baris_tabel:
    print("{:<15}{:<25}{:<25}{:<25}{:<25}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
hewan.close()