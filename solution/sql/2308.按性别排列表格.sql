SELECT user_id, gender
FROM (
    SELECT
        user_id,
        gender,
        ROW_NUMBER() OVER (PARTITION BY gender ORDER BY user_id) AS row_num,
        CASE gender
            WHEN 'female' THEN 1
            WHEN 'other' THEN 2
            ELSE 3
        END AS gender_order
    FROM Genders
) AS ordered_genders
ORDER BY row_num, gender_order;
