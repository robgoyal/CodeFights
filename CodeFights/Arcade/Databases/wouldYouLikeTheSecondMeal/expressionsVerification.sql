/* Name: expressionsVerification.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return the rows where (a operation b == c)
*/

CREATE PROCEDURE expressionsVerification()
BEGIN
    SELECT *
    FROM expressions
    WHERE CASE
            WHEN operation = '+' THEN (a + b = c)
            WHEN operation = '-' THEN (a - b = c)
            WHEN operation = '*' THEN (a * b = c)
            WHEN operation = '/' THEN (a / b = c)
        END;
END     