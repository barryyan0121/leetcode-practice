CREATE PROCEDURE UnpivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;
    SET @query = NULL;
    SELECT GROUP_CONCAT(
        CONCAT(
            'SELECT product_id, ', CHAR(39), column_name, CHAR(39),
            ' AS store, ', column_name,
            ' AS price FROM Products WHERE ', column_name, ' IS NOT NULL'
        ) SEPARATOR ' UNION ALL '
    ) INTO @query
    FROM information_schema.columns
    WHERE table_schema = DATABASE()
      AND table_name = 'Products'
      AND column_name <> 'product_id';

    PREPARE statement FROM @query;
    EXECUTE statement;
    DEALLOCATE PREPARE statement;
END;
