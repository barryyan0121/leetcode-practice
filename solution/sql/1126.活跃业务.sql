SELECT e.business_id
FROM Events AS e
JOIN (
    SELECT event_type, AVG(occurrences) AS average_occurrences
    FROM Events
    GROUP BY event_type
) AS averages ON averages.event_type = e.event_type
WHERE e.occurrences > averages.average_occurrences
GROUP BY e.business_id
HAVING COUNT(*) > 1;
