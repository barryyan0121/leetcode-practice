SELECT d.driver_id, COUNT(p.ride_id) AS cnt
FROM (SELECT DISTINCT driver_id FROM Rides) AS d
LEFT JOIN Rides AS p ON d.driver_id = p.passenger_id
GROUP BY d.driver_id;
