SELECT product_id, product_name, description
FROM products
WHERE REGEXP_LIKE(description, '(^|[^0-9A-Za-z])SN[0-9]{4}-[0-9]{4}(?![0-9A-Za-z])', 'c')
ORDER BY product_id;
