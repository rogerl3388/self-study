/*
Roger li 4/4/2024
SQL View practice
*/ 
-- CREATE VIEW V_avg_total AS
-- SELECT 
    -- avg(Total) AS [Average Total]
-- FROM
--     Invoice

-- DROP VIEW V_avg_total;

CREATE VIEW V_avg_total AS
SELECT
    round(avg(Total),2) AS [Average Total]
FROM
    Invoice