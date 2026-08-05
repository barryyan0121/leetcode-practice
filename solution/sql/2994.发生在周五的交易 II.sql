-- 2994. 发生在周五的交易 II
WITH RECURSIVE fridays AS (
    SELECT DATE('2023-11-03') AS purchase_date
    UNION ALL
    SELECT purchase_date + INTERVAL 7 DAY
    FROM fridays
    WHERE purchase_date < DATE('2023-11-24')
)
SELECT CEIL(DAYOFMONTH(f.purchase_date) / 7) AS week_of_month,
       f.purchase_date,
       COALESCE(SUM(p.amount_spend), 0) AS total_amount
FROM fridays f
LEFT JOIN Purchases p ON p.purchase_date = f.purchase_date
GROUP BY f.purchase_date
ORDER BY week_of_month;
