SELECT city_id, day, degree
FROM (
    SELECT city_id,
           day,
           degree,
           ROW_NUMBER() OVER (
               PARTITION BY city_id ORDER BY degree DESC, day
           ) AS row_number
    FROM Weather
) AS ranked
WHERE row_number = 1
ORDER BY city_id;
