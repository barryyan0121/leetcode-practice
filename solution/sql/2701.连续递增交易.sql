-- 2701. 连续递增交易
WITH marked AS (
    SELECT
        customer_id,
        transaction_date,
        amount,
        LAG(transaction_date) OVER (
            PARTITION BY customer_id ORDER BY transaction_date
        ) AS previous_date,
        LAG(amount) OVER (
            PARTITION BY customer_id ORDER BY transaction_date
        ) AS previous_amount
    FROM Transactions
), grouped AS (
    SELECT
        customer_id,
        transaction_date,
        SUM(
            CASE
                WHEN DATEDIFF(transaction_date, previous_date) = 1
                     AND amount > previous_amount THEN 0
                ELSE 1
            END
        ) OVER (PARTITION BY customer_id ORDER BY transaction_date) AS group_id
    FROM marked
)
SELECT customer_id, MIN(transaction_date) AS consecutive_start,
       MAX(transaction_date) AS consecutive_end
FROM grouped
GROUP BY customer_id, group_id
HAVING COUNT(*) >= 3
ORDER BY customer_id, consecutive_start;
