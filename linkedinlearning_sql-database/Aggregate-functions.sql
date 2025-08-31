/*
Roger 3/5/2024
Aggregate function practice, lesson follow-along
*/

SELECT
    SUM(Total) as [Total Sales],
    ROUND(AVG(Total),2) as [Average Sales],
    MAX(Total) as [Highest Sale],
    MIN(Total) as [Lowest Sale],
    COUNT(*) as [Sales Count]
FROM
    Invoice