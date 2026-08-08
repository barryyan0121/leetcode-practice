WITH ranked_orders AS (
    SELECT
        seller_id,
        item_id,
        ROW_NUMBER() OVER (PARTITION BY seller_id ORDER BY order_date) AS order_rank
    FROM Orders
)
SELECT
    users.user_id AS seller_id,
    IF(items.item_brand = users.favorite_brand, 'yes', 'no') AS 2nd_item_fav_brand
FROM Users AS users
LEFT JOIN ranked_orders
    ON ranked_orders.seller_id = users.user_id
    AND ranked_orders.order_rank = 2
LEFT JOIN Items AS items ON items.item_id = ranked_orders.item_id;
