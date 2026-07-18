SELECT ROUND(AVG(removed_posts * 100.0 / reported_posts), 2) AS average_daily_percent
FROM (
    SELECT a.action_date, COUNT(DISTINCT a.post_id) AS reported_posts,
           COUNT(DISTINCT r.post_id) AS removed_posts
    FROM Actions AS a
    LEFT JOIN Removals AS r ON r.post_id = a.post_id
    WHERE a.action = 'report' AND a.extra = 'spam'
    GROUP BY a.action_date
) AS daily;
