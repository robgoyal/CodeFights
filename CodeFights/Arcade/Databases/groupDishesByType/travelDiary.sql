/* Name: travelDiary.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return a semicolon separated list of all countries you've visited
*/

CREATE PROCEDURE travelDiary()
BEGIN
    SELECT GROUP_CONCAT(DISTINCT country ORDER BY country ASC SEPARATOR ';') as countries
    FROM diary;
END