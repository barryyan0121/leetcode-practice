WITH stats AS (
    SELECT user_id, COUNT(*) AS prompt_count, AVG(tokens) AS avg_tokens
    FROM prompts
    GROUP BY user_id
    HAVING COUNT(*) >= 3
), qualified AS (
    SELECT DISTINCT p.user_id
    FROM prompts p
    JOIN stats s ON s.user_id = p.user_id
    WHERE p.tokens > s.avg_tokens
)
SELECT s.user_id, s.prompt_count, ROUND(s.avg_tokens, 2) AS avg_tokens
FROM stats s
JOIN qualified q ON q.user_id = s.user_id
ORDER BY avg_tokens DESC, s.user_id;
