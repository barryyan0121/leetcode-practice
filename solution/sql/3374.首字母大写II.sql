WITH RECURSIVE Words AS (
    SELECT
        content_id,
        SUBSTRING_INDEX(content_text, ' ', 1) AS word,
        SUBSTRING(
            content_text,
            LENGTH(SUBSTRING_INDEX(content_text, ' ', 1)) + 2
        ) AS remaining_text,
        1 AS token_index
    FROM user_content
    UNION ALL
    SELECT
        content_id,
        SUBSTRING_INDEX(remaining_text, ' ', 1) AS word,
        SUBSTRING(
            remaining_text,
            LENGTH(SUBSTRING_INDEX(remaining_text, ' ', 1)) + 2
        ) AS remaining_text,
        token_index + 1 AS token_index
    FROM Words
    WHERE remaining_text != ''
),
Converted AS (
    SELECT
        content_id,
        GROUP_CONCAT(
            IF(
                LENGTH(word) - LENGTH(REPLACE(word, '-', '')) = 1
                AND LEFT(word, 1) <> '-',
                CONCAT(
                    UPPER(SUBSTRING(word, 1, 1)),
                    LOWER(SUBSTRING(word, 2, LOCATE('-', word) - 2)),
                    '-',
                    UPPER(SUBSTRING(SUBSTRING_INDEX(word, '-', -1), 1, 1)),
                    LOWER(SUBSTRING(SUBSTRING_INDEX(word, '-', -1), 2))
                ),
                CONCAT(UPPER(SUBSTRING(word, 1, 1)), LOWER(SUBSTRING(word, 2)))
            )
            ORDER BY token_index SEPARATOR ' '
        ) AS converted_text
    FROM Words
    GROUP BY content_id
)
SELECT
    user_content.content_id,
    user_content.content_text AS original_text,
    Converted.converted_text
FROM user_content
INNER JOIN Converted USING (content_id);
