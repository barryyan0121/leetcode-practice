WITH ranked AS (
    SELECT p.passenger_id,
           p.flight_id,
           p.booking_time,
           f.capacity,
           ROW_NUMBER() OVER (
               PARTITION BY p.flight_id ORDER BY p.booking_time
           ) AS booking_rank
    FROM Passengers p
    JOIN Flights f ON f.flight_id = p.flight_id
)
SELECT passenger_id,
       CASE WHEN booking_rank <= capacity THEN 'Confirmed' ELSE 'Waitlist' END AS Status
FROM ranked
ORDER BY passenger_id;
