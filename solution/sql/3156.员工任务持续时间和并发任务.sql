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
            ORDER BY t, delta
        ) AS concurrency,
        LEAD(t) OVER (
            PARTITION BY employee_id
            ORDER BY t, delta
        ) AS next_t
    FROM merged
),
dur AS (
    SELECT employee_id, FLOOR(SUM(TIMESTAMPDIFF(MINUTE, start_time, end_time)) / 60) AS total_duration
    FROM Tasks
    GROUP BY employee_id
),
mx AS (
    SELECT employee_id, MAX(concurrency) AS max_concurrent_tasks
    FROM scan
    GROUP BY employee_id
)
SELECT d.employee_id, d.total_duration, m.max_concurrent_tasks
FROM dur d
JOIN mx m USING (employee_id)
ORDER BY d.employee_id;
