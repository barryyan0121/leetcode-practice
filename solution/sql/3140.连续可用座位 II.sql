WITH free_seats AS (
    SELECT
        seat_id,
        seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) AS grp
    FROM Cinema
    WHERE free = 1
),
seat_groups AS (
    SELECT
        MIN(seat_id) AS first_seat_id,
        MAX(seat_id) AS last_seat_id,
        COUNT(*) AS consecutive_seats_len
    FROM free_seats
    GROUP BY grp
)
SELECT first_seat_id, last_seat_id, consecutive_seats_len
FROM seat_groups
WHERE consecutive_seats_len = (SELECT MAX(consecutive_seats_len) FROM seat_groups)
ORDER BY first_seat_id;
