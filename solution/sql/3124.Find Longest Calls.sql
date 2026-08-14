WITH T AS (
    SELECT
        first_name,
        type,
        duration,
        DATE_FORMAT(SEC_TO_TIME(duration), '%H:%i:%s') AS duration_formatted,
        RANK() OVER (PARTITION BY type ORDER BY duration DESC) AS rk
    FROM Calls
    JOIN Contacts ON Calls.contact_id = Contacts.id
)
SELECT first_name, type, duration_formatted
FROM T
WHERE rk <= 3
ORDER BY type DESC, duration DESC, first_name;
