-- 3252. 英超积分榜排名 II
WITH points AS (
    SELECT team_name,
           wins * 3 + draws AS points
    FROM TeamStats
), ranked AS (
    SELECT team_name,
           points,
           RANK() OVER (ORDER BY points DESC) AS position,
           COUNT(*) OVER () AS team_count
    FROM points
)
SELECT team_name,
       points,
       position,
       CASE
           WHEN position <= CEIL(team_count / 3) THEN 'Tier 1'
           WHEN position <= CEIL(team_count * 2 / 3) THEN 'Tier 2'
           ELSE 'Tier 3'
       END AS tier
FROM ranked
ORDER BY points DESC, team_name;
