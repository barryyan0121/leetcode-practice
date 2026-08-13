SELECT
  d.driver_name,
  ROUND(
    AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN t.distance_km / t.fuel_consumed END)
    OVER (PARTITION BY d.driver_id)
    -
    AVG(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN t.distance_km / t.fuel_consumed END)
    OVER (PARTITION BY d.driver_id)
  , 2) AS efficiency_improvement
FROM drivers d
JOIN trips t ON d.driver_id = t.driver_id
GROUP BY d.driver_id, d.driver_name
HAVING COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 1 AND 6 THEN 1 END) > 0
   AND COUNT(CASE WHEN MONTH(t.trip_date) BETWEEN 7 AND 12 THEN 1 END) > 0
ORDER BY efficiency_improvement DESC, d.driver_name ASC;
