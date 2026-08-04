WITH seasonal_sales AS (
    SELECT CASE
               WHEN MONTH(s.sale_date) IN (12, 1, 2) THEN 'Winter'
               WHEN MONTH(s.sale_date) IN (3, 4, 5) THEN 'Spring'
               WHEN MONTH(s.sale_date) IN (6, 7, 8) THEN 'Summer'
               ELSE 'Fall'
           END AS season,
           p.category,
           SUM(s.quantity) AS total_quantity,
           SUM(s.quantity * s.price) AS total_revenue
    FROM sales AS s
    JOIN products AS p ON p.product_id = s.product_id
    GROUP BY season, p.category
), ranked AS (
    SELECT seasonal_sales.*, ROW_NUMBER() OVER (
        PARTITION BY season
        ORDER BY total_quantity DESC, total_revenue DESC, category ASC
    ) AS ranking
    FROM seasonal_sales
)
SELECT season, category, total_quantity, total_revenue
FROM ranked
WHERE ranking = 1
ORDER BY season ASC;
