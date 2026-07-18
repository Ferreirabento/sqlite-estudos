import sqlite3

conn = sqlite3.connect("C:/Users/joaob/Documents/sqlite-estudos/banco.db")

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS alunos")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
