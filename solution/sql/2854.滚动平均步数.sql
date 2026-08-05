-- 2854. 滚动平均步数
SELECT s1.user_id,
       s1.steps_date,
       ROUND(AVG(s2.steps_count), 2) AS rolling_average
FROM Steps s1
JOIN Steps s2
  ON s1.user_id = s2.user_id
 AND s2.steps_date BETWEEN DATE_SUB(s1.steps_date, INTERVAL 2 DAY)
                         AND s1.steps_date
GROUP BY s1.user_id, s1.steps_date
HAVING COUNT(*) = 3
ORDER BY s1.user_id, s1.steps_date;
