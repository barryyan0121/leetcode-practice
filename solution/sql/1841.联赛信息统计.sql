WITH scores AS (
    SELECT
        home_team_id AS team_id,
        CASE
            WHEN home_team_goals > away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END AS points,
        home_team_goals AS goal_for,
        away_team_goals AS goal_against
    FROM Matches
    UNION ALL
    SELECT
        away_team_id,
        CASE
            WHEN home_team_goals < away_team_goals THEN 3
            WHEN home_team_goals = away_team_goals THEN 1
            ELSE 0
        END,
        away_team_goals,
        home_team_goals
    FROM Matches
) 
SELECT
    t.team_name,
    COUNT(*) AS matches_played,
    SUM(s.points) AS points,
    SUM(s.goal_for) AS goal_for,
    SUM(s.goal_against) AS goal_against,
    SUM(s.goal_for) - SUM(s.goal_against) AS goal_diff
FROM scores AS s
JOIN Teams AS t ON t.team_id = s.team_id
GROUP BY s.team_id, t.team_name
ORDER BY points DESC, goal_diff DESC, t.team_name;
