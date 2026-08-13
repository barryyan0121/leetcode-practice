WITH counts AS (
    SELECT city, HOUR(call_time) AS peak_calling_hour, COUNT(*) AS number_of_calls
    FROM Calls
    GROUP BY city, HOUR(call_time)
), ranked AS (
    SELECT *, MAX(number_of_calls) OVER (PARTITION BY city) AS max_calls
    FROM counts
)
SELECT city, peak_calling_hour, number_of_calls
FROM ranked
WHERE number_of_calls = max_calls
ORDER BY peak_calling_hour DESC, city DESC;
