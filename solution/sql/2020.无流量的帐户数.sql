SELECT COUNT(DISTINCT subscriptions.account_id) AS accounts_count
FROM Subscriptions AS subscriptions
LEFT JOIN Streams AS streams
    ON streams.account_id = subscriptions.account_id
    AND streams.stream_date BETWEEN '2021-01-01' AND '2021-12-31'
WHERE subscriptions.start_date <= '2021-12-31'
  AND subscriptions.end_date >= '2021-01-01'
  AND streams.session_id IS NULL;
