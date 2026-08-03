# @lc app=leetcode.cn id=1517 lang=mysql

SELECT user_id, name, mail
FROM Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c')
ORDER BY user_id;
