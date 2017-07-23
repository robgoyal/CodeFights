/* Name: countriesSelection.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return all rows with countries in Africa
*/

CREATE PROCEDURE countriesSelection()
BEGIN
    SELECT *
    FROM countries
    WHERE continent = 'Africa';
END