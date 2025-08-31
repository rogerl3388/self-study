/*
Roger, 03/03/2024: query from WSDA_music.db, following along with the lesson
*/
SELECT
    FirstName AS [Customer First Name],
    LastName AS "Customer Last Name",
    Email AS EMAIL
FROM
    Customer
ORDER BY
    FirstName ASC,
    LastName DESC
LIMIT 25