-- 2986. 找到第三笔交易
WITH ranked AS (
    SELECT user_id,
           spend,
           transaction_date,
           ROW_NUMBER() OVER (
               PARTITION BY user_id ORDER BY transaction_date
           ) AS row_number_
    FROM Transactions
)
SELECT user_id,
       MAX(CASE WHEN row_number_ = 3 THEN spend END) AS third_transaction_spend,
       MAX(CASE WHEN row_number_ = 3 THEN transaction_date END) AS third_transaction_date
FROM ranked
GROUP BY user_id
HAVING COUNT(*) >= 3
   AND MAX(CASE WHEN row_number_ = 3 THEN spend END)
       > MAX(CASE WHEN row_number_ = 1 THEN spend END)
   AND MAX(CASE WHEN row_number_ = 3 THEN spend END)
       > MAX(CASE WHEN row_number_ = 2 THEN spend END)
ORDER BY user_id;
