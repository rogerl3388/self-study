/* CHALLENGE QUESTION 2
Roger Li, 4/4/2024
Which customer has made the highest total purchase amount?
What is the total amount for each customer?
*/

SELECT
    c.CustomerId AS CustomerID, 
    c.FirstName AS FirstName,
    c.LastName AS LastName,
    SUM(i.Total) AS TotalPurchaseAmount
FROM
    Customer c
INNER JOIN
    Invoice i
ON
    c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName
ORDER BY TotalPurchaseAmount DESC