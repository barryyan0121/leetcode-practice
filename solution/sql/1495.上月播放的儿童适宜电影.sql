SELECT DISTINCT title
FROM TVProgram
JOIN Content USING (content_id)
WHERE program_date >= '2020-06-01'
  AND program_date < '2020-07-01'
  AND Kids_content = 'Y'
  AND content_type = 'Movies';
