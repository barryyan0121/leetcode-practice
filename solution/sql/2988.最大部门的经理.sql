-- 2988. 最大部门的经理
WITH department_counts AS (
    SELECT dep_id, COUNT(*) AS employee_count
    FROM Employees
    GROUP BY dep_id
)
SELECT e.emp_name AS manager_name, e.dep_id
FROM Employees e
JOIN department_counts d ON d.dep_id = e.dep_id
WHERE e.position = 'Manager'
  AND d.employee_count = (SELECT MAX(employee_count) FROM department_counts)
ORDER BY e.dep_id;
