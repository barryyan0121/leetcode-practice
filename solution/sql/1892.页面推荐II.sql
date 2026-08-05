WITH all_friendship AS (
    SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id FROM Friendship
)
SELECT friendship.user_id,
       likes.page_id,
       COUNT(*) AS friends_likes
FROM all_friendship AS friendship
JOIN Likes AS likes ON likes.user_id = friendship.friend_id
LEFT JOIN Likes AS own_likes
  ON own_likes.user_id = friendship.user_id
 AND own_likes.page_id = likes.page_id
WHERE own_likes.page_id IS NULL
GROUP BY friendship.user_id, likes.page_id;
