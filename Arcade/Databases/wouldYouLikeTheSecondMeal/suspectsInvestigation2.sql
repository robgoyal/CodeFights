/* Name: suspectsInvestigation2.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return the list of people who aren't suspects where their height is
            less than 170, surname isnt like Gre_n and first letter of name 
            doesn't start with B
*/

CREATE PROCEDURE suspectsInvestigation2()
BEGIN
    SELECT id, name, surname
    FROM Suspect
    WHERE NOT (height > 170 AND surname LIKE 'Gre_n' AND name LIKE 'B%');
END