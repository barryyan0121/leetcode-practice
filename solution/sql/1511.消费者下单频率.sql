SELECT c.customer_id, c.name
FROM Customers AS c
JOIN Orders AS o USING (customer_id)
JOIN Product AS p USING (product_id)
GROUP BY c.customer_id, c.name
HAVING SUM(IF(order_date >= '2020-06-01' AND order_date < '2020-07-01', quantity * price, 0)) >= 100
   AND SUM(IF(order_date >= '2020-07-01' AND order_date < '2020-08-01', quantity * price, 0)) >= 100;
