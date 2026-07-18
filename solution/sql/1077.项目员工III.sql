SELECT p.project_id, p.employee_id
FROM Project AS p
JOIN Employee AS e ON e.employee_id = p.employee_id
WHERE e.experience_years = (
    SELECT MAX(e2.experience_years)
    FROM Project AS p2
    JOIN Employee AS e2 ON e2.employee_id = p2.employee_id
    WHERE p2.project_id = p.project_id
);
