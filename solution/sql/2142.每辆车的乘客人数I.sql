SELECT b.bus_id,
       COUNT(p.passenger_id) AS passengers_cnt
FROM Buses AS b
LEFT JOIN Passengers AS p
  ON p.arrival_time <= b.arrival_time
 AND b.arrival_time = (
     SELECT MIN(b2.arrival_time)
     FROM Buses AS b2
     WHERE b2.arrival_time >= p.arrival_time
 )
GROUP BY b.bus_id
ORDER BY b.bus_id;
