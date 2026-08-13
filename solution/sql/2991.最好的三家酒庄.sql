WITH totals AS (
    SELECT country, winery, SUM(points) AS points
    FROM Wineries
    GROUP BY country, winery
), ranked AS (
    SELECT country, winery, points,
           ROW_NUMBER() OVER (
               PARTITION BY country ORDER BY points DESC, winery
           ) AS rank_no
    FROM totals
)
SELECT country,
       COALESCE(
           MAX(CASE WHEN rank_no = 1 THEN CONCAT(winery, ' (', points, ')') END),
           'No first winery'
       ) AS top_winery,
       COALESCE(
           MAX(CASE WHEN rank_no = 2 THEN CONCAT(winery, ' (', points, ')') END),
           'No second winery'
       ) AS second_winery,
       COALESCE(
           MAX(CASE WHEN rank_no = 3 THEN CONCAT(winery, ' (', points, ')') END),
           'No third winery'
       ) AS third_winery
FROM ranked
GROUP BY country
ORDER BY country;
