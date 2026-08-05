WITH user_totals AS (
    SELECT
        user_id,
        COUNT(DISTINCT content_id) AS content_count,
        COUNT(*) AS total_reactions
    FROM reactions
    GROUP BY user_id
), reaction_counts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS reaction_count
    FROM reactions
    GROUP BY user_id, reaction
), ranked AS (
    SELECT
        user_id,
        reaction,
        reaction_count,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY reaction_count DESC, reaction ASC
        ) AS reaction_rank
    FROM reaction_counts
)
SELECT
    r.user_id,
    r.reaction AS dominant_reaction,
    ROUND(r.reaction_count / t.total_reactions, 2) AS reaction_ratio
FROM ranked AS r
JOIN user_totals AS t ON t.user_id = r.user_id
WHERE r.reaction_rank = 1
  AND t.content_count >= 5
  AND r.reaction_count >= 0.6 * t.total_reactions
ORDER BY reaction_ratio DESC, r.user_id ASC;
