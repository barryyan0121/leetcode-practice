SELECT
    team_id,
    team_name,
    COALESCE(SUM(points), 0) AS num_points
FROM Teams
LEFT JOIN (
    SELECT
        host_team AS team_id,
        CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS points
    FROM Matches
    UNION ALL
    SELECT
        guest_team,
        CASE
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END
    FROM Matches
) AS scores USING (team_id)
GROUP BY team_id, team_name
ORDER BY num_points DESC, team_id;
