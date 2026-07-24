-- Quantos registros existem de cada sentimento.
SELECT DISTINCT(sentiment), COUNT(*) as frequencia 
FROM financial_sentiment_analysis
GROUP BY 1;


-- para saber quais das linhas são duplicatas
SELECT sentiment, sentence, COUNT(*) as contagens
FROM financial_sentiment_analysis
GROUP by 1, 2
HAVING COUNT(*) > 1;