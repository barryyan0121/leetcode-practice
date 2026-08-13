WITH team_avg AS (
    SELECT e.team, AVG(p.workload) AS avg_workload
    FROM Project p
    JOIN Employees e ON e.employee_id = p.employee_id
    GROUP BY e.team
)
SELECT p.employee_id, p.project_id, e.name AS employee_name,
       p.workload AS project_workload
FROM Project p
JOIN Employees e ON e.employee_id = p.employee_id
JOIN team_avg t ON t.team = e.team
WHERE p.workload > t.avg_workload
ORDER BY p.employee_id, p.project_id;
