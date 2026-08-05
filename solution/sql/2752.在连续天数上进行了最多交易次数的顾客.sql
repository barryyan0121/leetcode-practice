WITH dated AS (
    SELECT customer_id,
           transaction_date,
           DATE_SUB(transaction_date, INTERVAL ROW_NUMBER() OVER (
               PARTITION BY customer_id ORDER BY transaction_date
           ) DAY) AS grp
    FROM Transactions
), streaks AS (
    SELECT customer_id, COUNT(*) AS days
    FROM dated
    GROUP BY customer_id, grp
)
SELECT customer_id
FROM streaks
WHERE days = (SELECT MAX(days) FROM streaks)
ORDER BY customer_id;
