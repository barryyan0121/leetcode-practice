WITH RECURSIVE months AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1
    FROM months
    WHERE month < 12
)
SELECT m.month,
       (
           SELECT COUNT(*)
           FROM Drivers AS d
           WHERE d.join_date < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
       ) AS active_drivers,
       (
           SELECT COUNT(*)
           FROM Rides AS r
           JOIN AcceptedRides AS ar ON ar.ride_id = r.ride_id
           WHERE r.requested_at >= DATE_ADD('2020-01-01', INTERVAL m.month - 1 MONTH)
             AND r.requested_at < DATE_ADD('2020-01-01', INTERVAL m.month MONTH)
       ) AS accepted_rides
FROM months AS m
ORDER BY m.month;
