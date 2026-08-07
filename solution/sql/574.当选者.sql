--
-- @lc app=leetcode.cn id=574 lang=mysql
--
-- [574] 当选者
--

SELECT c.name
FROM Candidate AS c
JOIN Vote AS v ON v.CandidateId = c.id
GROUP BY c.id, c.name
ORDER BY COUNT(*) DESC
LIMIT 1;
