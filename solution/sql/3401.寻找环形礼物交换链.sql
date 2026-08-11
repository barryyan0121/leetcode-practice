WITH RECURSIVE valid_edges AS (
    SELECT s.*
    FROM SecretSanta AS s
    JOIN (
        SELECT giver_id
        FROM SecretSanta
        GROUP BY giver_id
        HAVING COUNT(*) = 1
    ) AS g ON g.giver_id = s.giver_id
    JOIN (
        SELECT receiver_id
        FROM SecretSanta
        GROUP BY receiver_id
        HAVING COUNT(*) = 1
    ) AS r ON r.receiver_id = s.receiver_id
), gift_chains AS (
    SELECT giver_id AS start_id,
           giver_id AS current_id,
           CAST(giver_id AS CHAR(2000)) AS path,
           0 AS chain_length,
           0 AS total_gift_value
    FROM valid_edges
    UNION ALL
    SELECT c.start_id,
           e.receiver_id,
           CONCAT(c.path, ',', e.receiver_id),
           c.chain_length + 1,
           c.total_gift_value + e.gift_value
    FROM gift_chains AS c
    JOIN valid_edges AS e ON e.giver_id = c.current_id
    WHERE FIND_IN_SET(e.receiver_id, c.path) = 0
), cycles AS (
    SELECT c.start_id,
           c.path,
           c.chain_length + 1 AS chain_length,
           c.total_gift_value + e.gift_value AS total_gift_value
    FROM gift_chains AS c
    JOIN valid_edges AS e ON e.giver_id = c.current_id
    WHERE e.receiver_id = c.start_id
), unique_cycles AS (
    SELECT c.chain_length, c.total_gift_value
    FROM cycles AS c
    WHERE NOT EXISTS (
        SELECT 1
        FROM valid_edges AS smaller
        WHERE smaller.giver_id < c.start_id
          AND FIND_IN_SET(smaller.giver_id, c.path) > 0
    )
)
SELECT ROW_NUMBER() OVER (ORDER BY chain_length DESC, total_gift_value DESC) AS chain_id,
       chain_length,
       total_gift_value
FROM unique_cycles
ORDER BY chain_length DESC, total_gift_value DESC;
