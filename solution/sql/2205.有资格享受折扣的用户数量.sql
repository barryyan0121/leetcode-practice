-- 2205. 有资格享受折扣的用户数量
SELECT COUNT(*) AS eligible_users
FROM Users
WHERE spend >= 100
  AND membership = 'Diamond'
   OR spend >= 1000
  AND membership = 'Gold';
