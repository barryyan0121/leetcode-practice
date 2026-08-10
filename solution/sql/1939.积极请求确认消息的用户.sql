SELECT DISTINCT first_confirmation.user_id
FROM Confirmations AS first_confirmation
JOIN Confirmations AS second_confirmation
  ON first_confirmation.user_id = second_confirmation.user_id
 AND first_confirmation.time_stamp < second_confirmation.time_stamp
WHERE TIMESTAMPDIFF(
    SECOND, first_confirmation.time_stamp, second_confirmation.time_stamp
) <= 24 * 60 * 60;
