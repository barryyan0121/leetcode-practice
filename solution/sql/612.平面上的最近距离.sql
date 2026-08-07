SELECT ROUND(
    SQRT(MIN(POW(a.x - b.x, 2) + POW(a.y - b.y, 2))),
    2
) AS shortest
FROM Point2D AS a
JOIN Point2D AS b ON a.x <> b.x OR a.y <> b.y;
