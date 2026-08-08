WITH scores AS (
    SELECT p.player_id, p.group_id,
           COALESCE(SUM(CASE WHEN m.first_player = p.player_id THEN m.first_score ELSE 0 END), 0)
           + COALESCE(SUM(CASE WHEN m.second_player = p.player_id THEN m.second_score ELSE 0 END), 0) AS score
    FROM Players p
    LEFT JOIN Matches m
      ON p.player_id = m.first_player OR p.player_id = m.second_player
    GROUP BY p.player_id, p.group_id
), ranked AS (
    SELECT group_id, player_id,
           ROW_NUMBER() OVER (PARTITION BY group_id ORDER BY score DESC, player_id) AS rn
    FROM scores
)
SELECT group_id, player_id
FROM ranked
WHERE rn = 1;
