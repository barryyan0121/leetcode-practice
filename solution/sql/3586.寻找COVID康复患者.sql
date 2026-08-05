WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
), first_recovery AS (
    SELECT p.patient_id, p.positive_date, MIN(t.test_date) AS negative_date
    FROM first_positive AS p
    JOIN covid_tests AS t
        ON t.patient_id = p.patient_id
       AND t.result = 'Negative'
       AND t.test_date > p.positive_date
    GROUP BY p.patient_id, p.positive_date
)
SELECT
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(r.negative_date, r.positive_date) AS recovery_time
FROM first_recovery AS r
JOIN patients AS p ON p.patient_id = r.patient_id
ORDER BY recovery_time ASC, p.patient_name ASC;
