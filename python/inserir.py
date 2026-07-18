import sqlite3

conn = sqlite3.connect("C:/Users/joaob/Documents/sqlite-estudos/banco.db")

cursor = conn.cursor()

cursor.execute("""INSERT INTO alunos(nome, idade) VALUE ('João',21), ('Maria',25), ('Carlos',18);""")


cursor.close()
