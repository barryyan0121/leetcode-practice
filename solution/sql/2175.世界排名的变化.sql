WITH old_ranks AS (
    SELECT team_id,
           ROW_NUMBER() OVER (ORDER BY points DESC, name) AS old_rank
    FROM TeamPoints
), new_ranks AS (
    SELECT t.team_id,
           ROW_NUMBER() OVER (
               ORDER BY t.points + p.points_change DESC, t.name
           ) AS new_rank
    FROM TeamPoints AS t
    JOIN PointsChange AS p ON p.team_id = t.team_id
)
SELECT t.team_id,
       t.name,
       CAST(old_ranks.old_rank AS SIGNED)
       - CAST(new_ranks.new_rank AS SIGNED) AS rank_diff
FROM TeamPoints AS t
JOIN old_ranks ON old_ranks.team_id = t.team_id
JOIN new_ranks ON new_ranks.team_id = t.team_id
ORDER BY t.team_id;
