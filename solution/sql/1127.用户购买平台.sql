WITH purchases AS (
    SELECT spend_date, user_id,
           CASE WHEN COUNT(*) = 2 THEN 'both' ELSE MAX(platform) END AS platform,
           SUM(amount) AS amount
    FROM Spending
    GROUP BY spend_date, user_id
), platforms AS (
    SELECT 'desktop' AS platform UNION ALL SELECT 'mobile' UNION ALL SELECT 'both'
)
SELECT dates.spend_date, platforms.platform,
       COALESCE(SUM(purchases.amount), 0) AS total_amount,
       COUNT(purchases.user_id) AS total_users
FROM (SELECT DISTINCT spend_date FROM Spending) AS dates
CROSS JOIN platforms
LEFT JOIN purchases ON purchases.spend_date = dates.spend_date AND purchases.platform = platforms.platform
GROUP BY dates.spend_date, platforms.platform
ORDER BY dates.spend_date, FIELD(platforms.platform, 'desktop', 'mobile', 'both');
