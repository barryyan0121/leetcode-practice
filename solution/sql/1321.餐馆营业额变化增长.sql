WITH daily AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
), rolling AS (
    SELECT visited_on,
           SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
           COUNT(*) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS days
    FROM daily
)
SELECT visited_on,
       amount,
       ROUND(amount / 7, 2) AS average_amount
FROM rolling
WHERE days = 7
ORDER BY visited_on;
