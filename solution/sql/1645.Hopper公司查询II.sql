WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
)
SELECT m.month,
       COALESCE(ROUND(
           100.0 * (
               SELECT COUNT(DISTINCT ar.driver_id)
               FROM Rides AS r
               JOIN AcceptedRides AS ar ON ar.ride_id = r.ride_id
               WHERE r.requested_at >= DATE_ADD('2020-01-01', INTERVAL m.month - 1 MONTH)
                 AND r.requested_at < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
           ) / NULLIF(
               (
                   SELECT COUNT(*)
                   FROM Drivers AS d
                   WHERE d.join_date < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
               ),
               0
           ),
           2
       ), 0) AS working_percentage
FROM months AS m
ORDER BY m.month;
