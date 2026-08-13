WITH RECURSIVE
    T AS (
        SELECT 1 AS week_of_month
        UNION ALL
        SELECT week_of_month + 1
        FROM T
        WHERE week_of_month < 4
    ),
    M AS (
        SELECT 'Premium' AS membership
        UNION ALL
        SELECT 'VIP'
    ),
    P AS (
        SELECT CEIL(DAYOFMONTH(purchase_date) / 7) AS week_of_month, membership, amount_spend
        FROM Purchases
        JOIN Users USING (user_id)
        WHERE DAYOFWEEK(purchase_date) = 6
          AND membership IN ('Premium', 'VIP')
    )
SELECT week_of_month, membership, IFNULL(SUM(amount_spend), 0) AS total_amount
FROM T
JOIN M
LEFT JOIN P USING (week_of_month, membership)
GROUP BY 1, 2
ORDER BY 1, 2;
