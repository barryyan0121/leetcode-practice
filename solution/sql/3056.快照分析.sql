-- 3056. 快照分析
SELECT a.age_bucket,
       ROUND(
           100 * SUM(CASE WHEN ac.activity_type = 'send' THEN ac.time_spent ELSE 0 END)
           / NULLIF(SUM(ac.time_spent), 0), 2
       ) AS send_perc,
       ROUND(
           100 * SUM(CASE WHEN ac.activity_type = 'open' THEN ac.time_spent ELSE 0 END)
           / NULLIF(SUM(ac.time_spent), 0), 2
       ) AS open_perc
FROM Age a
LEFT JOIN Activities ac ON ac.user_id = a.user_id
GROUP BY a.age_bucket;
