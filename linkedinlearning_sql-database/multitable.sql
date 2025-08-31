-- SQLite

/* SQLite Practice
Roger, 3/5/2024
*/

SELECT
    e.FirstName,
    e.LastName,
    c.FirstName,
    c.LastName,
    c.SupportRepId,
    i.CustomerId,
    i.Total
FROM
    Invoice as i
INNER JOIN
    Customer as c
ON
    i.CustomerId = c.CustomerId
INNER JOIN
    Employee as e
ON
    c.SupportRepId = e.EmployeeID
ORDER BY
    i.Total DESC
LIMIT 15