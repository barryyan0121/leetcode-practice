WITH yearly AS (
    SELECT product_id, YEAR(purchase_date) AS purchase_year
    FROM Orders
    GROUP BY product_id, YEAR(purchase_date)
    HAVING COUNT(*) >= 3
)
SELECT DISTINCT first_year.product_id
FROM yearly AS first_year
JOIN yearly AS next_year
  ON next_year.product_id = first_year.product_id
 AND next_year.purchase_year = first_year.purchase_year + 1;
