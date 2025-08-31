/*
Roger 3/5/2024
Date functions, follow along
*/

SELECT
    LastName,
    FirstName,
    BirthDate,
    STRFTIME("%Y-%m-%d",BirthDate) as [Bday date only],
    STRFTIME("%Y-%m-%d","now") - STRFTIME("%Y-%m-%d",BirthDate) AS [Age]
FROM
    Employee