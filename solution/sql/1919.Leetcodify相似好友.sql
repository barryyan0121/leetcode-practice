SELECT DISTINCT friendship.user1_id, friendship.user2_id
FROM Friendship AS friendship
JOIN Listens AS first_listens
  ON friendship.user1_id = first_listens.user_id
JOIN Listens AS second_listens
  ON friendship.user2_id = second_listens.user_id
 AND first_listens.song_id = second_listens.song_id
 AND first_listens.day = second_listens.day
GROUP BY friendship.user1_id, friendship.user2_id, first_listens.day
HAVING COUNT(DISTINCT first_listens.song_id) >= 3;
