WITH RECURSIVE ranked_buses AS (
    SELECT bus_id,
           arrival_time,
           capacity,
           ROW_NUMBER() OVER (ORDER BY arrival_time, bus_id) AS rn
    FROM Buses
), boarded (rn, bus_id, passengers_cnt, total_boarded) AS (
    SELECT r.rn,
           r.bus_id,
           LEAST(r.capacity, (
               SELECT COUNT(*)
               FROM Passengers AS p
               WHERE p.arrival_time <= r.arrival_time
           )),
           LEAST(r.capacity, (
               SELECT COUNT(*)
               FROM Passengers AS p
               WHERE p.arrival_time <= r.arrival_time
           ))
    FROM ranked_buses AS r
    WHERE r.rn = 1
    UNION ALL
    SELECT r.rn,
           r.bus_id,
           LEAST(r.capacity, (
               SELECT COUNT(*)
               FROM Passengers AS p
               WHERE p.arrival_time <= r.arrival_time
           ) - b.total_boarded),
           b.total_boarded + LEAST(r.capacity, (
               SELECT COUNT(*)
               FROM Passengers AS p
               WHERE p.arrival_time <= r.arrival_time
           ) - b.total_boarded)
    FROM boarded AS b
    JOIN ranked_buses AS r ON r.rn = b.rn + 1
)
SELECT bus_id, passengers_cnt
FROM boarded
ORDER BY bus_id;
