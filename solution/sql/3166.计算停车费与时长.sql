WITH per_lot AS (
    SELECT
        car_id,
        lot_id,
        SUM(fee_paid) AS total_fee,
        SUM(TIMESTAMPDIFF(MINUTE, entry_time, exit_time)) AS total_minutes
    FROM ParkingTransactions
    GROUP BY car_id, lot_id
),
best_lot AS (
    SELECT
        car_id,
        lot_id,
        ROW_NUMBER() OVER (
            PARTITION BY car_id
            ORDER BY total_minutes DESC, lot_id
        ) AS rn
    FROM per_lot
)
SELECT
    p.car_id,
    SUM(p.total_fee) AS total_fee_paid,
    ROUND(SUM(p.total_fee) / SUM(p.total_minutes) * 60, 2) AS avg_hourly_fee,
    b.lot_id AS parking_lot_id
FROM per_lot p
JOIN best_lot b ON p.car_id = b.car_id AND p.lot_id = b.lot_id AND b.rn = 1
GROUP BY p.car_id, b.lot_id
ORDER BY p.car_id;
