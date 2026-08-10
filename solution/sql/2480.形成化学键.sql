SELECT metal.symbol AS metal, nonmetal.symbol AS nonmetal
FROM Elements AS metal
JOIN Elements AS nonmetal ON metal.type = 'Metal' AND nonmetal.type = 'Nonmetal';
