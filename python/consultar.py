import sqlite3

conn = sqlite3.connect("C:/Users/joaob/Documents/sqlite-estudos/banco.db")

cursor = conn.cursor()

cursor.execute("SELECT Sentence, Sentiment FROM financial_sentiment_analysis LIMIT 100;")

for coisa in cursor.fetchall():
    print(coisa)

conn.close()