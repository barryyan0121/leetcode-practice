WITH edges AS (
    SELECT user_id1 AS user_id, user_id2 AS friend_id FROM Friends
    UNION ALL
    SELECT user_id2, user_id1 FROM Friends
)
SELECT f.user_id1, f.user_id2
FROM Friends f
WHERE NOT EXISTS (
    SELECT 1
    FROM edges a
    JOIN edges b ON b.friend_id = a.friend_id
    WHERE a.user_id = f.user_id1 AND b.user_id = f.user_id2
)
ORDER BY f.user_id1, f.user_id2;
