WITH counts AS (
    SELECT o.seller_id, COUNT(DISTINCT o.item_id) AS num_items
    FROM Orders o
    JOIN Items i ON i.item_id = o.item_id
    JOIN Users u ON u.seller_id = o.seller_id
    WHERE i.item_brand <> u.favorite_brand
    GROUP BY o.seller_id
)
SELECT seller_id, num_items
FROM counts
WHERE num_items = (SELECT MAX(num_items) FROM counts)
ORDER BY seller_id;
