SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales AS s
JOIN (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) AS first_sales ON first_sales.product_id = s.product_id AND first_sales.first_year = s.year;
