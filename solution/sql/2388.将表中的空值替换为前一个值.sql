WITH g AS (
    SELECT *, COUNT(drink) OVER (ORDER BY id) AS grp
    FROM CoffeeShop
)
SELECT id, MAX(drink) OVER (PARTITION BY grp) AS drink
FROM g;
