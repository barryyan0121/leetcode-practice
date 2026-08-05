-- 1990. 统计实验的数量
WITH platforms AS (
    SELECT 'Android' AS platform UNION ALL SELECT 'IOS' UNION ALL SELECT 'Web'
), names AS (
    SELECT 'Reading' AS experiment_name UNION ALL SELECT 'Sports' UNION ALL SELECT 'Programming'
)
SELECT p.platform, n.experiment_name, COUNT(e.experiment_id) AS num_experiments
FROM platforms p
CROSS JOIN names n
LEFT JOIN Experiments e
  ON e.platform = p.platform AND e.experiment_name = n.experiment_name
GROUP BY p.platform, n.experiment_name;
