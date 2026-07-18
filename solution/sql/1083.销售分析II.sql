SELECT s.buyer_id
FROM Sales AS s
JOIN Product AS p ON p.product_id = s.product_id
GROUP BY s.buyer_id
HAVING SUM(p.product_name = 'S8') > 0
   AND SUM(p.product_name = 'iPhone') = 0;
