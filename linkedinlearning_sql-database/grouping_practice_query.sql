/*
Roger 3/7/2024
Follow along: filtering groups
*/

SELECT
    BillingCountry,
    BillingCity,
    ROUND(AVG(Total),2) as [AveragePrice]
FROM
    Invoice
-- WHERE
--     BillingCity LIKE "B%"
GROUP BY
    BillingCountry,
    BillingCity
-- HAVING
--     AveragePrice > 5
ORDER BY
    BillingCountry,
    BillingCity