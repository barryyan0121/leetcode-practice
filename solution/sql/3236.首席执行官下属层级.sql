WITH RECURSIVE hierarchy AS (
    SELECT
        employee_id,
        employee_name,
        salary,
        0 AS hierarchy_level,
        salary AS ceo_salary
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id,
        e.employee_name,
        e.salary,
        h.hierarchy_level + 1,
        h.ceo_salary
    FROM hierarchy AS h
    JOIN Employees AS e
        ON e.manager_id = h.employee_id
)
SELECT
    employee_id AS subordinate_id,
    employee_name AS subordinate_name,
    hierarchy_level,
    salary - ceo_salary AS salary_difference
FROM hierarchy
WHERE hierarchy_level > 0
ORDER BY hierarchy_level, subordinate_id;
