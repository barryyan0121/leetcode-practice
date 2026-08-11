WITH s AS (
    SELECT s.user_id, s.product_id, SUM(s.quantity * p.price) AS spending
    FROM Sales s JOIN Product p ON p.product_id = s.product_id
    GROUP BY s.user_id, s.product_id
), r AS (
    SELECT *, RANK() OVER (PARTITION BY user_id ORDER BY spending DESC) AS rk
    FROM s
)
SELECT user_id, product_id
FROM r
WHERE rk = 1;
