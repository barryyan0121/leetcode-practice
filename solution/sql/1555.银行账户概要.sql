WITH changes AS (
    SELECT paid_to AS user_id, amount AS delta FROM Transactions
    UNION ALL
    SELECT paid_by, -amount FROM Transactions
), balances AS (
    SELECT u.user_id, u.user_name, u.credit + COALESCE(SUM(delta), 0) AS credit
    FROM Users AS u
    LEFT JOIN changes AS c USING (user_id)
    GROUP BY u.user_id, u.user_name, u.credit
)
SELECT *, IF(credit < 0, 'Yes', 'No') AS credit_limit_breached
FROM balances;
