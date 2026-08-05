SELECT b.bus_id,
       COUNT(p.passenger_id) AS passengers_cnt
FROM Buses AS b
LEFT JOIN Passengers AS p
  ON p.arrival_time <= b.arrival_time
 AND p.arrival_time > COALESCE(
     (SELECT MAX(previous.arrival_time)
      FROM Buses AS previous
      WHERE previous.arrival_time < b.arrival_time), -1
 )
GROUP BY b.bus_id
ORDER BY b.bus_id;
