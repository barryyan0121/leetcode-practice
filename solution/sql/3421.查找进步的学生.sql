WITH RankedScores AS (
    SELECT
        student_id,
        subject,
        score,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date
        ) AS first_rank,
        ROW_NUMBER() OVER (
            PARTITION BY student_id, subject
            ORDER BY exam_date DESC
        ) AS latest_rank,
        COUNT(*) OVER (PARTITION BY student_id, subject) AS exam_count
    FROM Scores
)
SELECT
    first_score.student_id,
    first_score.subject,
    first_score.score AS first_score,
    latest_score.score AS latest_score
FROM RankedScores
GROUP BY student_id, subject
HAVING MAX(exam_count) >= 2
    AND MAX(CASE WHEN first_rank = 1 THEN score END)
        < MAX(CASE WHEN latest_rank = 1 THEN score END)
ORDER BY student_id, subject;
