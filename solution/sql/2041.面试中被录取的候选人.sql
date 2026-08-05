-- 2041. 面试中被录取的候选人
SELECT c.candidate_id
FROM Candidates c
JOIN Rounds r ON r.interview_id = c.interview_id
WHERE c.years_of_exp >= 2
GROUP BY c.candidate_id
HAVING SUM(r.score) > 15;
