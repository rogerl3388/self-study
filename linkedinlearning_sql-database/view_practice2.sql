/*
Roger Li 2024-04-04

View practice 2
*/
CREATE VIEW V_Tracks_InvoiceLine AS
SELECT
    il.InvoiceId,
    il.UnitPrice,
    il.Quantity,
    t.Name,
    t.Composer,
    t.Milliseconds
FROM
    InvoiceLine AS il
INNER JOIN
    Track AS t
ON
    il.TrackID = t.TrackId