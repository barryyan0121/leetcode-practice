WITH feb AS (
    SELECT user_id, DAY(post_date) AS d
    FROM Posts
    WHERE post_date >= '2024-02-01' AND post_date < '2024-03-01'
), counts AS (
    SELECT user_id, COUNT(*) AS total_posts
    FROM feb
    GROUP BY user_id
), windows AS (
    SELECT a.user_id, a.d, COUNT(b.d) AS posts_7
    FROM feb a
    LEFT JOIN feb b
      ON b.user_id = a.user_id AND b.d BETWEEN a.d AND a.d + 6
    GROUP BY a.user_id, a.d
), best AS (
    SELECT user_id, MAX(posts_7) AS max_7day_posts
    FROM windows
    GROUP BY user_id
)
SELECT b.user_id, b.max_7day_posts,
       ROUND(c.total_posts / 4, 4) AS avg_weekly_posts
FROM best b
JOIN counts c ON c.user_id = b.user_id
WHERE b.max_7day_posts >= c.total_posts / 2
ORDER BY b.user_id;
