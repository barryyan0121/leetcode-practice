SELECT
    t.team_name,
    COUNT(m.team_id) AS matches_played,
    COALESCE(SUM(m.points), 0) AS points,
    COALESCE(SUM(m.goal_for), 0) AS goal_for,
    COALESCE(SUM(m.goal_against), 0) AS goal_against,
    COALESCE(SUM(m.goal_for - m.goal_against), 0) AS goal_diff
FROM Teams AS t
LEFT JOIN (
    SELECT
        home_team_id AS team_id,
        home_team_goals AS goal_for,
        away_team_goals AS goal_against,
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END AS points
    FROM Matches
    UNION ALL
    SELECT
        away_team_id,
        away_team_goals,
        home_team_goals,
        CASE
            WHEN away_team_goals > home_team_goals THEN 3
            WHEN away_team_goals = home_team_goals THEN 1
            ELSE 0
        END
    FROM Matches
) AS m ON m.team_id = t.team_id
GROUP BY t.team_id, t.team_name
ORDER BY points DESC, goal_diff DESC, t.team_name;
