SELECT activity
FROM Friends
GROUP BY activity
HAVING COUNT(*) > (
    SELECT MIN(counts.participants)
    FROM (SELECT COUNT(*) AS participants FROM Friends GROUP BY activity) AS counts
)
AND COUNT(*) < (
    SELECT MAX(counts.participants)
    FROM (SELECT COUNT(*) AS participants FROM Friends GROUP BY activity) AS counts
);
