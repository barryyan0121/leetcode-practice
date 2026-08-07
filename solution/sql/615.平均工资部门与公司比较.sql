WITH company AS (
    SELECT DATE_FORMAT(pay_date, '%Y-%m') AS pay_month, AVG(amount) AS avg_amount
    FROM Salary
    GROUP BY DATE_FORMAT(pay_date, '%Y-%m')
), department AS (
    SELECT DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month,
           e.department_id,
           AVG(s.amount) AS avg_amount
    FROM Salary AS s
    JOIN Employee AS e ON e.employee_id = s.employee_id
    GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m'), e.department_id
)
SELECT d.pay_month,
       d.department_id,
       CASE
           WHEN d.avg_amount > c.avg_amount THEN 'higher'
           WHEN d.avg_amount < c.avg_amount THEN 'lower'
           ELSE 'same'
       END AS comparison
FROM department AS d
JOIN company AS c ON c.pay_month = d.pay_month;
