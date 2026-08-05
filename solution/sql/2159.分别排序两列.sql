WITH ranked_first AS (
    SELECT first_col, ROW_NUMBER() OVER (ORDER BY first_col) AS row_number
    FROM Data
), ranked_second AS (
    SELECT second_col, ROW_NUMBER() OVER (ORDER BY second_col DESC) AS row_number
    FROM Data
)
SELECT first_col, second_col
FROM ranked_first
JOIN ranked_second USING (row_number);
