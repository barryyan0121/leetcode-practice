WITH category_stats AS (
    SELECT
        t.customer_id,
        p.category,
        SUM(t.amount) AS category_amount,
        COUNT(*) AS category_transactions,
        MAX(t.transaction_date) AS last_transaction_date
    FROM Transactions AS t
    JOIN Products AS p
        ON p.product_id = t.product_id
    GROUP BY t.customer_id, p.category
), ranked_categories AS (
    SELECT
        category_stats.*,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY category_transactions DESC, last_transaction_date DESC
        ) AS category_rank
    FROM category_stats
)
SELECT
    customer_id,
    ROUND(SUM(category_amount), 2) AS total_amount,
    SUM(category_transactions) AS transaction_count,
    COUNT(*) AS unique_categories,
    ROUND(SUM(category_amount) / SUM(category_transactions), 2)
        AS avg_transaction_amount,
    MAX(CASE WHEN category_rank = 1 THEN category END) AS top_category,
    ROUND(
        SUM(category_transactions) * 10 + SUM(category_amount) / 100,
        2
    ) AS loyalty_score
FROM ranked_categories
GROUP BY customer_id
ORDER BY loyalty_score DESC, customer_id ASC;
