WITH t AS (
    SELECT
        c1.contact_id,
        c2.first_name,
        c1.type,
        c1.duration,
        ROW_NUMBER() OVER (
            PARTITION BY c1.type
            ORDER BY c1.duration DESC, c2.first_name DESC
        ) AS rn
    FROM Calls c1
    JOIN Contacts c2
      ON c1.contact_id = c2.id
)
SELECT
    first_name,
    type,
    DATE_FORMAT(SEC_TO_TIME(duration), '%H:%i:%s') AS duration_formatted
FROM t
WHERE rn <= 3
ORDER BY type, duration DESC, first_name DESC;
