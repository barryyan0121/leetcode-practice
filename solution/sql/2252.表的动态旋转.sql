CREATE PROCEDURE PivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;
    SET @columns = NULL;
    SELECT GROUP_CONCAT(
        DISTINCT CONCAT(
            'MAX(IF(store = ', CHAR(39), store,
            CHAR(39), ', price, NULL)) AS ', store
        ) ORDER BY store
    ) INTO @columns
    FROM Products;

    SET @query = CONCAT(
        'SELECT product_id, ', @columns,
        ' FROM Products GROUP BY product_id'
    );
    PREPARE statement FROM @query;
    EXECUTE statement;
    DEALLOCATE PREPARE statement;
END;
