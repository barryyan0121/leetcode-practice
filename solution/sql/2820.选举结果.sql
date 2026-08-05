WITH scored AS (
    SELECT candidate,
           SUM(1.0 / voter_count) AS votes
    FROM (
        SELECT voter, candidate,
               COUNT(*) OVER (PARTITION BY voter) AS voter_count
        FROM Votes
    ) AS v
    GROUP BY candidate
)
SELECT candidate
FROM scored
WHERE votes = (SELECT MAX(votes) FROM scored)
ORDER BY candidate;
