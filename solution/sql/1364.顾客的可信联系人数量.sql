SELECT
    i.invoice_id,
    c.customer_name,
    i.price,
    COUNT(ct.user_id) AS contacts_cnt,
    COUNT(trusted.customer_id) AS trusted_contacts_cnt
FROM Invoices AS i
JOIN Customers AS c ON c.customer_id = i.user_id
LEFT JOIN Contacts AS ct ON ct.user_id = i.user_id
LEFT JOIN Customers AS trusted ON trusted.email = ct.contact_email
GROUP BY i.invoice_id, c.customer_name, i.price
ORDER BY i.invoice_id;
