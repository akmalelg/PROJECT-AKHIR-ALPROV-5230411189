import sqlite3
hewan = sqlite3.connect('database_fauna.db')

hewan.execute('''
              CREATE TABLE FAUNA(
              id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
              nama_fauna VARCHAR(50),
              jenis VARCHAR(50),
              asal VARCHAR(50),
              jumlah_skrg INTEGER(10),
              tahun_ditemukan INTEGER(10)       
              )
              ''')
hewan.close()
