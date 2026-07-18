import pandas as pd
import sqlite3

conn = sqlite3.connect("C:/Users/joaob/Documents/sqlite-estudos/banco.db")

df = pd.read_csv("C:/Users/joaob/Documents/sqlite-estudos/datasets/financial_sentiment_analysis.csv")

df.to_sql("financial_sentiment_analysis", conn, if_exists="replace", index=False)
