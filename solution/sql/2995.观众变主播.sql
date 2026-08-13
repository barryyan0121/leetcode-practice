WITH first_session AS (
    SELECT user_id, session_type,
           ROW_NUMBER() OVER (
               PARTITION BY user_id ORDER BY session_start
           ) AS rn
    FROM Sessions
), counts AS (
    SELECT s.user_id, COUNT(*) AS sessions_count
    FROM Sessions s
    JOIN first_session f
      ON f.user_id = s.user_id AND f.rn = 1
    WHERE f.session_type = 'Viewer' AND s.session_type = 'Streamer'
    GROUP BY s.user_id
)
SELECT user_id, sessions_count
FROM counts
ORDER BY sessions_count DESC, user_id DESC;
