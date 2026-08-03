SELECT login_date, COUNT(*) AS user_count
FROM (
    SELECT user_id, MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
) AS first_logins
WHERE DATEDIFF('2019-06-30', login_date) BETWEEN 0 AND 90
GROUP BY login_date;
