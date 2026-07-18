import sqlite3

conn = sqlite3.connect("banco.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE alunos ( id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER) ")

cursor.close()