-- achando duplicatas
SELECT records,
       COUNT(*)
FROM (
    SELECT sentence,
           sentiment,
           COUNT(*) AS records
    FROM financial_sentiment_analysis
    GROUP BY sentence, sentiment
) a
WHERE records > 1
GROUP BY records
ORDER BY records;