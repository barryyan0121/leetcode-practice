WITH merged AS (
    SELECT
        employee_id,
        start_time AS t,
        1 AS delta
    FROM Tasks
    UNION ALL
    SELECT
        employee_id,
        end_time AS t,
        -1 AS delta
    FROM Tasks
),
scan AS (
    SELECT
        employee_id,
        t,
        SUM(delta) OVER (
            PARTITION BY employee_id
            ORDER BY t, delta DESC
            ROWS UNBOUNDED PRECEDING
        ) AS concurrency,
        LEAD(t) OVER (
            PARTITION BY employee_id
            ORDER BY t, delta DESC
        ) AS next_t
    FROM merged
),
dur AS (
    SELECT
        employee_id,
        FLOOR(
            SUM(
                CASE
                    WHEN concurrency > 0
                    THEN TIMESTAMPDIFF(SECOND, t, next_t)
                    ELSE 0
                END
            ) / 3600
        ) AS total_task_hours
    FROM scan
    GROUP BY employee_id
),
mx AS (
    SELECT employee_id, MAX(concurrency) AS max_concurrent_tasks
    FROM scan
    GROUP BY employee_id
)
SELECT d.employee_id, d.total_task_hours, m.max_concurrent_tasks
FROM dur d
JOIN mx m USING (employee_id)
ORDER BY d.employee_id;
