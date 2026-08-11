SELECT id,
       CASE WHEN drink IS NULL THEN @last ELSE @last := drink END AS drink
FROM CoffeeShop, (SELECT @last := NULL) AS init;
