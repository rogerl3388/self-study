/*
Roger, 3/5/2024
Function practice, lesson follow along
*/

SELECT
    FirstName,
    LastName,
    Address,
    FirstName || " " || LastName || " " || Address || ", " || City || ", "|| State || " " || PostalCode AS [Mailing Address],
    -- LENGTH(PostalCode),
    SUBSTR(PostalCode, 1, 5) AS [5-digit Postal Code],
    UPPER(FirstName) as [First Name Caps],
    LOWER(LastName) as [Last Name Lower]
FROM
    Customer
WHERE
    Country = "USA"