WITH driver_stats AS (
    SELECT v.fuel_type,
           d.driver_id,
           ROUND(AVG(t.rating), 2) AS rating,
           SUM(t.distance) AS distance,
           d.accidents
    FROM Drivers AS d
    JOIN Vehicles AS v ON v.driver_id = d.driver_id
    JOIN Trips AS t ON t.vehicle_id = v.vehicle_id
    GROUP BY v.fuel_type, d.driver_id, d.accidents
), ranked AS (
    SELECT fuel_type,
           driver_id,
           rating,
           distance,
           ROW_NUMBER() OVER (
               PARTITION BY fuel_type
               ORDER BY rating DESC, distance DESC, accidents, driver_id
           ) AS rn
    FROM driver_stats
)
SELECT fuel_type, driver_id, rating, distance
FROM ranked
WHERE rn = 1
ORDER BY fuel_type;
