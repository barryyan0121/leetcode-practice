SELECT e1.emp_id, e1.month, SUM(e2.salary) AS salary
FROM Employee e1
JOIN Employee e2
  ON e2.emp_id = e1.emp_id
 AND e2.month BETWEEN e1.month - 2 AND e1.month
WHERE e1.month <> (
    SELECT MAX(e3.month)
    FROM Employee e3
    WHERE e3.emp_id = e1.emp_id
)
GROUP BY e1.emp_id, e1.month
ORDER BY e1.emp_id, e1.month DESC;
