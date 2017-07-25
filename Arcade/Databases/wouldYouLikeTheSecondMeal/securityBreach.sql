/* Name: securityBreach.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return columns where the attribute has the following format
            <one or more characters>%<firstname>_<lastname>%<zero or more chars>
*/

CREATE PROCEDURE securityBreach()
BEGIN
    SELECT *
    FROM users
    WHERE attribute LIKE BINARY CONCAT('%_!%', first_name, '_', second_name, '!%%') ESCAPE '!';
END