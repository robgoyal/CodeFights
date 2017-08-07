/* Name: mostExpensive.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the product with the lexicographically smallest name
            with the largest amount of money spent
*/

CREATE PROCEDURE mostExpensive()
BEGIN
    SELECT MIN(name) as name
    FROM Products
    GROUP BY (price * quantity)
    ORDER BY (price * quantity) DESC
    LIMIT 1;
END