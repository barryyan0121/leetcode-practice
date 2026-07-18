SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT MAX(employee_count)
    FROM (
        SELECT COUNT(*) AS employee_count
        FROM Project
        GROUP BY project_id
    ) AS counts
);
