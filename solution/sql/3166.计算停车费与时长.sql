WITH per_lot AS (
    SELECT car_id, lot_id,
           SUM(fee_paid) AS total_fee,
           SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time)) AS total_minutes
    FROM ParkingTransactions
    GROUP BY car_id, lot_id
),
best_lot AS (
    SELECT car_id, lot_id,
           ROW_NUMBER() OVER (
               PARTITION BY car_id
               ORDER BY total_minutes DESC, lot_id
           ) AS rn
    FROM per_lot
),
totals AS (
    SELECT car_id,
           SUM(total_fee) AS total_fee_paid,
           SUM(total_minutes) AS total_minutes
    FROM per_lot
    GROUP BY car_id
)
SELECT t.car_id,
       t.total_fee_paid,
       ROUND(t.total_fee_paid / t.total_minutes * 60, 2) AS avg_hourly_fee,
       b.lot_id AS most_time_lot
FROM totals t
JOIN best_lot b ON t.car_id = b.car_id AND b.rn = 1
ORDER BY t.car_id;
