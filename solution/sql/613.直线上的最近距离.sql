SELECT MIN(ABS(a.x - b.x)) AS shortest
FROM Point AS a
JOIN Point AS b ON a.x <> b.x;
