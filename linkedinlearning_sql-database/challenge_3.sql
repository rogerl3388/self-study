/*
Roger Li, 4/4/2024
CHALLENGE 3: Which employees have the highest number of customers
they provide support to, and how many customers does each employee support?
*/

SELECT
    e.EmployeeID,
    e.FirstName, e.LastName,
    COUNT(c.SupportRepId) as NumberOfCustomers
FROM Employee e
INNER JOIN Customer c
ON e.EmployeeID = c.SupportRepId
GROUP BY e.EmployeeID
ORDER BY NumberOfCustomers DESC