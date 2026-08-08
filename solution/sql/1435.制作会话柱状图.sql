SELECT '[0-5>' AS bin, COUNT(IF(duration < 300, 1, NULL)) AS total
FROM Sessions
UNION ALL
SELECT '[5-10>', COUNT(IF(duration BETWEEN 300 AND 599, 1, NULL))
FROM Sessions
UNION ALL
SELECT '[10-15>', COUNT(IF(duration BETWEEN 600 AND 899, 1, NULL))
FROM Sessions
UNION ALL
SELECT '15 or more', COUNT(IF(duration >= 900, 1, NULL))
FROM Sessions;
