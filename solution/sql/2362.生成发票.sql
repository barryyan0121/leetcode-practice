WITH invoice_totals AS (
    SELECT invoice_id, SUM(quantity * price) AS total
    FROM Purchases
    JOIN Products USING (product_id)
    GROUP BY invoice_id
), chosen AS (
    SELECT invoice_id
    FROM invoice_totals
    ORDER BY total DESC, invoice_id
    LIMIT 1
)
SELECT p.product_id,
       SUM(p.quantity) AS quantity,
       SUM(p.quantity * pr.price) AS price
FROM Purchases AS p
JOIN Products AS pr USING (product_id)
JOIN chosen AS c USING (invoice_id)
GROUP BY p.product_id;
