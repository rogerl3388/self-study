/*
Roger 3/7/2024
Subquery practice
*/
SELECT
    InvoiceDate,
    BillingAddress,
    BillingCity,
    Total
FROM
    Invoice
WHERE
    Total <
        (SELECT
            ROUND( AVG(Total) , 2 )
        FROM
            Invoice)
ORDER BY
    Total DESC