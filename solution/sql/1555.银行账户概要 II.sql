# @lc app=leetcode.cn id=1555 lang=mysql

SELECT u.name, SUM(t.amount) AS balance
FROM Users AS u
JOIN Transactions AS t ON t.account = u.account
GROUP BY u.account, u.name
HAVING SUM(t.amount) > 10000;
