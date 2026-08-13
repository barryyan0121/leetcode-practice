WITH session_differences AS (
    SELECT user_id,
           session_start,
           LAG(session_end) OVER (
               PARTITION BY user_id, session_type
               ORDER BY session_start
           ) AS prev_session_end
    FROM Sessions
)
SELECT DISTINCT user_id
FROM session_differences
WHERE TIMESTAMPDIFF(HOUR, prev_session_end, session_start) <= 12
ORDER BY user_id;
