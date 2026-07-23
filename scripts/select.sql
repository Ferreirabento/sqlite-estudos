-- Quantos registros existem de cada sentimento.
SELECT DISTINCT(sentiment), COUNT(*) as frequencia 
FROM financial_sentiment_analysis
GROUP BY 1;
