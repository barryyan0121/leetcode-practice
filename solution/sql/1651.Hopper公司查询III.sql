WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 10
)
SELECT m.month,
       ROUND(
           COALESCE(SUM(ar.ride_distance), 0) / 3,
           2
       ) AS average_ride_distance,
       ROUND(
           COALESCE(SUM(ar.ride_duration), 0) / 3,
           2
       ) AS average_ride_duration
FROM months AS m
LEFT JOIN Rides AS r
    ON r.requested_at >= DATE_ADD('2020-01-01', INTERVAL m.month - 1 MONTH)
   AND r.requested_at < DATE_ADD('2020-01-01', INTERVAL m.month + 2 MONTH)
LEFT JOIN AcceptedRides AS ar ON ar.ride_id = r.ride_id
GROUP BY m.month
ORDER BY m.month;
