WITH friendships AS (
    SELECT user1_id, user2_id FROM Friendship
    UNION
    SELECT user2_id, user1_id FROM Friendship
)
SELECT DISTINCT first_listens.user_id, second_listens.user_id AS recommended_id
FROM Listens AS first_listens
JOIN Listens AS second_listens
  ON first_listens.day = second_listens.day
 AND first_listens.song_id = second_listens.song_id
 AND first_listens.user_id <> second_listens.user_id
WHERE NOT EXISTS (
    SELECT 1
    FROM friendships
    WHERE friendships.user1_id = first_listens.user_id
      AND friendships.user2_id = second_listens.user_id
)
GROUP BY first_listens.day, first_listens.user_id, second_listens.user_id
HAVING COUNT(DISTINCT first_listens.song_id) >= 3;
