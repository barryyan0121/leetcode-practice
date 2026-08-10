WITH grouped AS (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary) AS team_id
    FROM Employees
    GROUP BY salary
    HAVING COUNT(*) >= 2
)
SELECT e.employee_id, e.name, e.salary, g.team_id
FROM Employees AS e
JOIN grouped AS g ON g.salary = e.salary
ORDER BY g.team_id, e.employee_id;
