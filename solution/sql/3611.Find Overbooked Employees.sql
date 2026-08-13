WITH weekly AS (
    SELECT
        e.employee_id,
        e.employee_name,
        e.department,
        STRFTIME('%Y-%W', m.meeting_date) AS week_id,
        SUM(m.duration_hours) AS total_hours
    FROM employees e
    JOIN meetings m ON e.employee_id = m.employee_id
    GROUP BY e.employee_id, e.employee_name, e.department, STRFTIME('%Y-%W', m.meeting_date)
)
SELECT
    employee_id,
    employee_name,
    department,
    COUNT(*) AS meeting_heavy_weeks
FROM weekly
WHERE total_hours > 20
GROUP BY employee_id, employee_name, department
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, employee_name ASC;
