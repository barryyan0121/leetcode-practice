WITH RECURSIVE customer_years AS (
    SELECT customer_id,
           YEAR(MIN(order_date)) AS first_year,
           YEAR(MAX(order_date)) AS last_year,
           YEAR(MIN(order_date)) AS purchase_year
    FROM Orders
    GROUP BY customer_id
    UNION ALL
    SELECT customer_id, first_year, last_year, purchase_year + 1
    FROM customer_years
    WHERE purchase_year < last_year
), yearly AS (
    SELECT customer_id, YEAR(order_date) AS purchase_year, SUM(price) AS total
    FROM Orders
    GROUP BY customer_id, YEAR(order_date)
), totals AS (
    SELECT cy.customer_id,
           cy.purchase_year,
           COALESCE(y.total, 0) AS total,
           LAG(COALESCE(y.total, 0)) OVER (
               PARTITION BY cy.customer_id ORDER BY cy.purchase_year
           ) AS previous_total
    FROM customer_years AS cy
    LEFT JOIN yearly AS y
      ON y.customer_id = cy.customer_id
     AND y.purchase_year = cy.purchase_year
)
SELECT customer_id
FROM totals
GROUP BY customer_id
HAVING COUNT(*) = 1
    OR SUM(total > previous_total) = COUNT(*) - 1;
