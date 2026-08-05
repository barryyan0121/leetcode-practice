WITH traffic AS (
    SELECT departure_airport AS airport_id, flights_count FROM Flights
    UNION ALL
    SELECT arrival_airport AS airport_id, flights_count FROM Flights
), totals AS (
    SELECT airport_id, SUM(flights_count) AS total
    FROM traffic
    GROUP BY airport_id
)
SELECT airport_id
FROM totals
WHERE total = (SELECT MAX(total) FROM totals);
