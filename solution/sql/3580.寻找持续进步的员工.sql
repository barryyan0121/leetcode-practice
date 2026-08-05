WITH ranked AS (
    SELECT
        employee_id,
        rating,
        ROW_NUMBER() OVER (
            PARTITION BY employee_id ORDER BY review_date DESC
        ) AS recent
    FROM performance_reviews
), recent_three AS (
    SELECT
        employee_id,
        MAX(CASE WHEN recent = 1 THEN rating END) AS latest_rating,
        MAX(CASE WHEN recent = 2 THEN rating END) AS middle_rating,
        MAX(CASE WHEN recent = 3 THEN rating END) AS earliest_rating
    FROM ranked
    WHERE recent <= 3
    GROUP BY employee_id
)
SELECT
    r.employee_id,
    e.name,
    r.latest_rating - r.earliest_rating AS improvement_score
FROM recent_three AS r
JOIN employees AS e ON e.employee_id = r.employee_id
WHERE r.latest_rating > r.middle_rating
  AND r.middle_rating > r.earliest_rating
ORDER BY improvement_score DESC, e.name ASC;
