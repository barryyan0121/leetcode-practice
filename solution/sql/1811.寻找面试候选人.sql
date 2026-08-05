WITH medals AS (
    SELECT contest_id, gold_medal AS user_id FROM Contests
    UNION ALL
    SELECT contest_id, silver_medal AS user_id FROM Contests
    UNION ALL
    SELECT contest_id, bronze_medal AS user_id FROM Contests
),
consecutive AS (
    SELECT user_id
    FROM (
        SELECT user_id,
               contest_id - ROW_NUMBER() OVER (
                   PARTITION BY user_id ORDER BY contest_id
               ) AS group_id
        FROM medals
    ) grouped_medals
    GROUP BY user_id, group_id
    HAVING COUNT(*) >= 3
),
gold_medals AS (
    SELECT gold_medal AS user_id
    FROM Contests
    GROUP BY gold_medal
    HAVING COUNT(*) >= 3
),
candidates AS (
    SELECT user_id FROM consecutive
    UNION
    SELECT user_id FROM gold_medals
)
SELECT Users.name, Users.mail
FROM Users
JOIN candidates ON candidates.user_id = Users.user_id;
