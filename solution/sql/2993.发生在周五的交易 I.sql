-- 2993. 发生在周五的交易 I
SELECT CEIL(DAYOFMONTH(purchase_date) / 7) AS week_of_month,
       purchase_date,
       SUM(amount_spend) AS total_amount
FROM Purchases
WHERE DAYOFWEEK(purchase_date) = 6
GROUP BY purchase_date
ORDER BY week_of_month;
