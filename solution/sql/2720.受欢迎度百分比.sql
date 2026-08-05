WITH users AS (
    SELECT user1 AS id, user2 AS other_id FROM Friends
    UNION
    SELECT user2, user1 FROM Friends
)
SELECT id AS user1,
       ROUND(COUNT(DISTINCT other_id) * 100.0 / (SELECT COUNT(*) FROM (SELECT DISTINCT id FROM users) AS all_users), 2) AS percentage_popularity
FROM users
GROUP BY id
ORDER BY id;
