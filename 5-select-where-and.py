import sqlite3
hewan = sqlite3.connect('database_fauna.db')

cur = hewan.cursor()
cur.execute("SELECT * FROM FAUNA WHERE JENIS = 'mamalia' and ASAL = 'sulawesi' ")
baris_tabel = cur.fetchall()

print("DATA HEWAN JENIS MAMALIA DAN ASAL SULAWESI 2023")
print('-'*135)
print("{:<15}{:<25}{:<25}{:<25}{:<25}".format("ID FAUNA", "JENIS", "NAMA FAUNA", "ASAL", "JUMLAH SEKARANG", "TAHUN DI TEMUKAN"))
print('-'*135)

for baris in baris_tabel:
    print("{:<15}{:<25}{:<25}{:<25}{:<25}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
hewan.close()