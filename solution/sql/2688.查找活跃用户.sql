-- 2688. 查找活跃用户
SELECT DISTINCT user_id
FROM Users
WHERE user_id IN (
    SELECT u1.user_id
    FROM Users u1
    JOIN Users u2
      ON u1.user_id = u2.user_id
     AND u2.created_at > u1.created_at
     AND DATEDIFF(u2.created_at, u1.created_at) <= 7
);
