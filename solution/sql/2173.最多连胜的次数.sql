WITH grouped AS (
    SELECT player_id,
           result,
           ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_day)
             - ROW_NUMBER() OVER (PARTITION BY player_id, result ORDER BY match_day) AS streak_group
    FROM Matches
), wins AS (
    SELECT player_id, streak_group, COUNT(*) AS streak
    FROM grouped
    WHERE result = 'Win'
    GROUP BY player_id, streak_group
)
SELECT players.player_id, COALESCE(MAX(wins.streak), 0) AS longest_streak
FROM (SELECT DISTINCT player_id FROM Matches) AS players
LEFT JOIN wins ON wins.player_id = players.player_id
GROUP BY players.player_id;
