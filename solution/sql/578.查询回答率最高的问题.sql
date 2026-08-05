SELECT question_id AS survey_log
FROM SurveyLog
GROUP BY question_id
ORDER BY COUNT(answer_id) / COUNT(*) DESC
LIMIT 1;
