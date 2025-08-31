/*
Roger 03/03/2024:
Filtering and labeling practice
*/

SELECT
    InvoiceDate,
    BillingAddress,
    BillingCity,
    total,
    CASE
        WHEN total < 2.00 THEN "Baseline Purchase"
        WHEN total BETWEEN 2.00 AND 6.99 THEN "Low Purchase"
        WHEN total BETWEEN 7.00 AND 15.00 THEN "Target"
        ELSE "Top Performer"
    END AS PurchaseType
FROM
    Invoice
WHERE
    -- total BETWEEN 1.98 AND 5.00
    -- total IN (1.98, 3.96) AND
    -- BillingCity = "Brussels"
    -- BillingCity IN ("Brussels", "Paris", "Orlando")
    -- BillingCity LIKE "%b%"
    -- DATE(InvoiceDate) > "2010-05-22" AND
    -- Total < 3.00
    -- Total > 1.98 AND
    -- (BillingCity LIKE "P%" OR BillingCity LIKE "D%")
    PurchaseType = "Top Performer"
ORDER BY
    BillingCity