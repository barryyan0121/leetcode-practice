-- 3586. 寻找 COVID 康复患者
WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
), first_recovery AS (
    SELECT p.patient_id,
           p.positive_date,
           MIN(t.test_date) AS negative_date
    FROM first_positive p
    JOIN covid_tests t
      ON t.patient_id = p.patient_id
     AND t.result = 'Negative'
     AND t.test_date > p.positive_date
    GROUP BY p.patient_id, p.positive_date
)
SELECT p.patient_id,
       p.patient_name,
       p.age,
       DATEDIFF(r.negative_date, r.positive_date) AS recovery_time
FROM patients p
JOIN first_recovery r ON r.patient_id = p.patient_id
ORDER BY recovery_time, p.patient_name;
