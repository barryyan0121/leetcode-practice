SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
FROM Queries AS q
LEFT JOIN NPV AS n ON q.id = n.id AND q.year = n.year;
