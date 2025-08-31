/*
Roger 3/7/2024
Subquery Practice 3, follow along
*/

SELECT
    InvoiceDate,
    BillingAddress,
    BillingCity
FROM
    Invoice
WHERE
    InvoiceDate IN
    (SELECT InvoiceDate
    FROM Invoice
    WHERE InvoiceID IN (251, 252, 254))
ORDER BY
    InvoiceDate