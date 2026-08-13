WITH RECURSIVE t1 AS (
    SELECT
        tweet_id,
        SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(tweet, '#', 2), '#', -1), ' ', 1) AS tag,
        TRIM(LEADING SUBSTRING_INDEX(tweet, '#', 2) FROM tweet) AS remain_tags
    FROM Tweets
    WHERE tweet LIKE '%#%' AND YEAR(tweet_date) = 2024 AND MONTH(tweet_date) = 2
    UNION ALL
    SELECT
        tweet_id,
        SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(remain_tags, '#', 2), '#', -1), ' ', 1) AS tag,
        TRIM(LEADING SUBSTRING_INDEX(remain_tags, '#', 2) FROM remain_tags) AS remain_tags
    FROM t1
    WHERE remain_tags LIKE '%#%'
)
SELECT CONCAT('#', tag) AS hashtag, COUNT(*) AS count
FROM t1
GROUP BY tag
ORDER BY count DESC, hashtag DESC
LIMIT 3;
