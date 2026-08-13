WITH bounds AS (
    SELECT id, height,
           MAX(height) OVER (ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS left_max,
           MAX(height) OVER (ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS right_max
    FROM Heights
)
SELECT SUM(GREATEST(0, LEAST(left_max, right_max) - height)) AS total_trapped_water
FROM bounds;
