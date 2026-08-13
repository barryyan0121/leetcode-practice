SELECT DISTINCT c.X, c.Y
FROM Coordinates c
WHERE (
          c.X < c.Y
          AND EXISTS (
              SELECT 1
              FROM Coordinates r
              WHERE r.X = c.Y AND r.Y = c.X
          )
      )
   OR (
          c.X = c.Y
          AND (
              SELECT COUNT(*)
              FROM Coordinates r
              WHERE r.X = c.X AND r.Y = c.Y
          ) >= 2
      )
ORDER BY c.X, c.Y;
