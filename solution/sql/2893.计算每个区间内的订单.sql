-- 2893. 计算每个区间内的订单
SELECT FLOOR((minute - 1) / 6) + 1 AS interval_no,
       SUM(order_count) AS total_orders
FROM Orders
GROUP BY interval_no
ORDER BY interval_no;
