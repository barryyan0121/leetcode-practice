-- 3103. 查找热门话题标签 II
WITH RECURSIVE tags AS (
    SELECT tweet,
           REGEXP_SUBSTR(tweet, '#[0-9A-Za-z_]+', 1, 1) AS hashtag,
           1 AS occurrence
    FROM Tweets
    UNION ALL
    SELECT tweet,
           REGEXP_SUBSTR(tweet, '#[0-9A-Za-z_]+', 1, occurrence + 1),
           occurrence + 1
    FROM tags
    WHERE hashtag IS NOT NULL
)
SELECT hashtag, COUNT(*) AS count
FROM tags
WHERE hashtag IS NOT NULL
GROUP BY hashtag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
