WITH monthly_income AS (
    SELECT account_id,
           CAST(DATE_FORMAT(day, '%Y-%m-01') AS DATE) AS month_start,
           SUM(amount) AS income
    FROM Transactions
    WHERE type = 'Creditor'
    GROUP BY account_id, month_start
)
SELECT DISTINCT current.account_id
FROM monthly_income AS current
JOIN monthly_income AS following
  ON following.account_id = current.account_id
 AND following.month_start = DATE_ADD(current.month_start, INTERVAL 1 MONTH)
JOIN Accounts
  ON Accounts.account_id = current.account_id
WHERE current.income > Accounts.max_income
  AND following.income > Accounts.max_income;
