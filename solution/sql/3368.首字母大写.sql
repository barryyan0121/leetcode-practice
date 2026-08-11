WITH RECURSIVE chars AS (
    SELECT content_id, content_text, 1 AS position
    FROM user_content
    UNION ALL
    SELECT content_id, content_text, position + 1
    FROM chars
    WHERE position < CHAR_LENGTH(content_text)
)
SELECT content_id,
       content_text AS original_text,
       GROUP_CONCAT(
           IF(position = 1 OR SUBSTRING(content_text, position - 1, 1) = ' ',
              UPPER(SUBSTRING(content_text, position, 1)),
              LOWER(SUBSTRING(content_text, position, 1))
           )
           ORDER BY position SEPARATOR ''
       ) AS converted_text
FROM chars
GROUP BY content_id, content_text;
