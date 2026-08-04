WITH RECURSIVE hierarchy AS (
    SELECT employee_id, employee_name, manager_id, salary, 1 AS employee_level
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.employee_name, e.manager_id, e.salary,
           h.employee_level + 1
    FROM Employees e
    JOIN hierarchy h ON e.manager_id = h.employee_id
), relations AS (
    SELECT employee_id AS manager_id, employee_id, salary
    FROM Employees
    UNION ALL
    SELECT r.manager_id, e.employee_id, e.salary
    FROM relations r
    JOIN Employees e ON e.manager_id = r.employee_id
)
SELECT h.employee_id,
       h.employee_name,
       h.employee_level AS level,
       COUNT(r.employee_id) - 1 AS team_size,
       SUM(r.salary) AS budget
FROM hierarchy h
JOIN relations r ON r.manager_id = h.employee_id
GROUP BY h.employee_id, h.employee_name, h.employee_level
ORDER BY h.employee_level, budget DESC, h.employee_name;
