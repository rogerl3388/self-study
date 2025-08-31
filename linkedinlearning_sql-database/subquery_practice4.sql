/*
Roger 3/7/2024
Subquery practice: DISTINCT
*/

SELECT
    TrackId,
    Composer,
    Name
FROM
    Track
WHERE
    TrackId NOT IN (
        SELECT
            DISTINCT
            TrackID
        FROM
            InvoiceLine
        ORDER BY
            TrackID
    )
