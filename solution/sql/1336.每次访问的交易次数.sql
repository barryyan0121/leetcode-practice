WITH RECURSIVE visit_counts AS (
    SELECT v.user_id, v.visit_date, COUNT(t.transaction_date) AS transactions_count
    FROM Visits AS v
    LEFT JOIN Transactions AS t
        ON v.user_id = t.user_id AND v.visit_date = t.transaction_date
    GROUP BY v.user_id, v.visit_date
), numbers AS (
    SELECT 0 AS transactions_count
    UNION ALL
    SELECT transactions_count + 1
    FROM numbers
    WHERE transactions_count < (SELECT MAX(transactions_count) FROM visit_counts)
)
SELECT n.transactions_count, COUNT(v.transactions_count) AS visits_count
FROM numbers AS n
LEFT JOIN visit_counts AS v ON n.transactions_count = v.transactions_count
GROUP BY n.transactions_count
ORDER BY n.transactions_count;
