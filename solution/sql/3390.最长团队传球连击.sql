WITH ordered AS (
    SELECT source.team_name,
           p.time_stamp,
           CASE WHEN source.team_name = target.team_name THEN 1 ELSE 0 END AS success
    FROM Passes AS p
    JOIN Teams AS source ON source.player_id = p.pass_from
    JOIN Teams AS target ON target.player_id = p.pass_to
), grouped AS (
    SELECT team_name,
           success,
           SUM(CASE WHEN success = 0 THEN 1 ELSE 0 END) OVER (
               PARTITION BY team_name ORDER BY time_stamp
           ) AS streak_group
    FROM ordered
), streaks AS (
    SELECT team_name, streak_group, SUM(success) AS streak
    FROM grouped
    GROUP BY team_name, streak_group
), teams AS (
    SELECT DISTINCT team_name FROM Teams
)
SELECT teams.team_name,
       COALESCE(MAX(streaks.streak), 0) AS longest_streak
FROM teams
LEFT JOIN streaks ON streaks.team_name = teams.team_name
GROUP BY teams.team_name
ORDER BY teams.team_name;
