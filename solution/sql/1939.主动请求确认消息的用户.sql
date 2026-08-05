-- 1939. 主动请求确认消息的用户
SELECT user_id
FROM Confirmations
GROUP BY user_id
HAVING COUNT(*) >= 2
   AND TIMESTAMPDIFF(HOUR, MIN(time), MAX(time)) <= 24;
