WITH grouped AS (
    SELECT item_type, SUM(square_footage) AS area, COUNT(*) AS item_count
    FROM Inventory
    GROUP BY item_type
), prime AS (
    SELECT area, item_count, FLOOR(500000 / area) AS units
    FROM grouped
    WHERE item_type = 'prime_eligible'
), other AS (
    SELECT SUM(area) AS area, SUM(item_count) AS item_count
    FROM grouped
    WHERE item_type <> 'prime_eligible'
)
SELECT 'prime_eligible' AS item_type, units * item_count AS item_count
FROM prime
UNION ALL
SELECT 'not_prime',
       FLOOR((500000 - units * area) / other.area) * other.item_count
FROM prime
CROSS JOIN other
ORDER BY item_count DESC;
