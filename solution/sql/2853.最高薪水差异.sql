-- 2853. 最高薪水差异
SELECT ABS(
    MAX(CASE WHEN department = 'Engineering' THEN salary END)
    - MAX(CASE WHEN department = 'Marketing' THEN salary END)
) AS salary_difference
FROM Salaries;
