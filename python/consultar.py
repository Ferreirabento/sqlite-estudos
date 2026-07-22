import sqlite3

conn = sqlite3.connect("C:/Users/joaob/Documents/sqlite-estudos/banco.db")

cursor = conn.cursor()

limitar = cursor.execute("SELECT Sentence, Sentiment FROM financial_sentiment_analysis LIMIT 100;")
#print(limitar.fetchall())

frequencia = cursor.execute("SELECT distinct(Sentiment), count(*) as qualidade FROM financial_sentiment_analysis GROUP BY 1;")
print(frequencia.fetchall())

conn.close()