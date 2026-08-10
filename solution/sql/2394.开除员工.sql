SELECT e.employee_id
FROM Employees AS e
LEFT JOIN Logs AS l USING (employee_id)
GROUP BY e.employee_id, e.needed_hours
HAVING COALESCE(
           SUM(CEIL(TIMESTAMPDIFF(SECOND, l.in_time, l.out_time) / 60)),
           0
       ) < e.needed_hours * 60;
