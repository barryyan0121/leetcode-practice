SELECT
    posts.sub_id AS post_id,
    COUNT(DISTINCT comments.sub_id) AS number_of_comments
FROM Submissions AS posts
LEFT JOIN Submissions AS comments ON posts.sub_id = comments.parent_id
WHERE posts.parent_id IS NULL
GROUP BY posts.sub_id
ORDER BY post_id;
