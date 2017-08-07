/* Name: marketReport.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return a table with the country name and number of competitors from
            the country. The last row should have the total number of competitors
            in the format 'Total: #'
*/

CREATE PROCEDURE marketReport()
BEGIN
    SELECT IFNULL(country, 'Total:') AS country, COUNT(country) AS competitors
    FROM foreignCompetitors
    GROUP BY country ASC WITH ROLLUP;
END