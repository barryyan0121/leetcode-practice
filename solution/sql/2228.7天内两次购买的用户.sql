-- 2228. 7 天内两次购买的用户
SELECT DISTINCT p1.user_id
FROM Purchases AS p1
JOIN Purchases AS p2
  ON p1.user_id = p2.user_id
 AND p1.purchase_date <= p2.purchase_date
 AND (p1.purchase_date < p2.purchase_date OR p1.purchase_id < p2.purchase_id)
 AND DATEDIFF(p2.purchase_date, p1.purchase_date) <= 7
ORDER BY p1.user_id;
