WITH RECURSIVE halves AS (
    SELECT 1 AS half_number
    UNION ALL
    SELECT 2
), scores AS (
    SELECT t.team_name,
           CASE WHEN p.time_stamp <= '45:00' THEN 1 ELSE 2 END AS half_number,
           CASE WHEN source.team_name = target.team_name THEN 1 ELSE -1 END AS score
    FROM Passes AS p
    JOIN Teams AS source ON source.player_id = p.pass_from
    JOIN Teams AS target ON target.player_id = p.pass_to
    JOIN Teams AS t ON t.player_id = p.pass_from
), teams AS (
    SELECT DISTINCT team_name FROM Teams
)
SELECT teams.team_name,
       halves.half_number,
       COALESCE(SUM(scores.score), 0) AS dominance
FROM teams
CROSS JOIN halves
LEFT JOIN scores ON scores.team_name = teams.team_name
                 AND scores.half_number = halves.half_number
GROUP BY teams.team_name, halves.half_number
ORDER BY teams.team_name, halves.half_number;
