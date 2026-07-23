SELECT DISTINCT(sentence), COUNT(*) as frequencia 
FROM financial_sentiment_analysis
GROUP BY 1;