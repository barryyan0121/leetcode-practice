SELECT DISTINCT user_id
FROM (
    SELECT
        user_id,
        created_at,
        LAG(created_at) OVER (
            PARTITION BY user_id
            ORDER BY created_at
        ) AS previous_created_at
    FROM Users
) AS purchases
WHERE DATEDIFF(created_at, previous_created_at) <= 7;
