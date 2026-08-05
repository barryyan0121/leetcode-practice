WITH senior_candidates AS (
    SELECT employee_id, salary,
           SUM(salary) OVER (ORDER BY salary, employee_id) AS total_salary
    FROM Candidates
    WHERE experience = 'Senior'
),
senior_count AS (
    SELECT SUM(total_salary <= 70000) AS accepted,
           COALESCE(MAX(CASE WHEN total_salary <= 70000 THEN total_salary ELSE 0 END), 0) AS spent
    FROM senior_candidates
),
junior_candidates AS (
    SELECT employee_id, salary,
           SUM(salary) OVER (ORDER BY salary, employee_id) AS total_salary
    FROM Candidates
    WHERE experience = 'Junior'
),
junior_count AS (
    SELECT COUNT(*) AS accepted
    FROM junior_candidates
    WHERE total_salary <= 70000 - (SELECT spent FROM senior_count)
)
SELECT 'Senior' AS experience, accepted AS accepted_candidates
FROM senior_count
UNION ALL
SELECT 'Junior', accepted
FROM junior_count;
