SELECT
    ad_id,
    IFNULL(
        ROUND(
            100 * SUM(action = 'Clicked')
            / NULLIF(SUM(action IN ('Clicked', 'Viewed')), 0),
            2
        ),
        0
    ) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id;
