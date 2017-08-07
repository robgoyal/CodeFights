/* Name: countriesInfo.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return a table which contains the number of countries along with
            average and total population
*/

CREATE PROCEDURE countriesInfo()
BEGIN
    SELECT COUNT(name) as number, AVG(population) as average, SUM(population) as total
    FROM countries;
END