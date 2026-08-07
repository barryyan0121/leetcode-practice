SELECT f1.followee AS follower, COUNT(DISTINCT f1.follower) AS num
FROM Follow AS f1
JOIN Follow AS f2 ON f1.followee = f2.follower
GROUP BY f1.followee
ORDER BY f1.followee;
