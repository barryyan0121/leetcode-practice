WITH ranked AS (
    SELECT policy_id, state, fraud_score,
           RANK() OVER (PARTITION BY state ORDER BY fraud_score DESC) AS rn,
           COUNT(*) OVER (PARTITION BY state) AS cnt
    FROM Fraud
)
SELECT policy_id, state, fraud_score
FROM ranked
WHERE rn <= GREATEST(1, CEIL(cnt * 0.05))
ORDER BY state, fraud_score DESC, policy_id;
