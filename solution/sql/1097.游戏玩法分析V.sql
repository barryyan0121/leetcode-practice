SELECT
    a.event_date AS install_dt,
    COUNT(*) AS installs,
    ROUND(COUNT(b.player_id) / COUNT(*), 2) AS Day1_retention
FROM Activity AS a
LEFT JOIN Activity AS b
    ON b.player_id = a.player_id
    AND b.event_date = DATE_ADD(a.event_date, INTERVAL 1 DAY)
WHERE a.event_date = (
    SELECT MIN(event_date)
    FROM Activity
    WHERE player_id = a.player_id
)
GROUP BY a.event_date;
