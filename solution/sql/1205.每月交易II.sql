SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    SUM(state = 'approved') AS approved_count,
    SUM(IF(state = 'approved', amount, 0)) AS approved_amount,
    SUM(state = 'chargeback') AS chargeback_count,
    SUM(IF(state = 'chargeback', amount, 0)) AS chargeback_amount
FROM (
    SELECT trans_date, country, state, amount
    FROM Transactions
    WHERE state = 'approved'
    UNION ALL
    SELECT chargebacks.trans_date, transactions.country, 'chargeback', transactions.amount
    FROM Chargebacks AS chargebacks
    JOIN Transactions AS transactions ON transactions.id = chargebacks.trans_id
) AS records
GROUP BY month, country;
