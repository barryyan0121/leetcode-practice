WITH marked AS (
    SELECT hall_id,
           start_day,
           end_day,
           MAX(end_day) OVER (
               PARTITION BY hall_id
               ORDER BY start_day, end_day
               ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
           ) AS previous_end
    FROM HallEvents
), grouped AS (
    SELECT hall_id,
           start_day,
           end_day,
           SUM(
               CASE WHEN previous_end IS NULL OR start_day > previous_end THEN 1 ELSE 0 END
           ) OVER (
               PARTITION BY hall_id ORDER BY start_day, end_day
           ) AS group_id
    FROM marked
)
SELECT hall_id, MIN(start_day) AS start_day, MAX(end_day) AS end_day
FROM grouped
GROUP BY hall_id, group_id;
