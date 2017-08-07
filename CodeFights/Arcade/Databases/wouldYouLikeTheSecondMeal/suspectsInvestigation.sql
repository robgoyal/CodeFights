/* Name: suspectsInvestigation.sql
   Author: Robin Goyal
   Last-Modified: July 25, 2017
   Purpose: Return the list of suspects who are shorter than 170, the first
            letter of the name is B and the format of the last name is
            Gre?n.
*/

CREATE PROCEDURE suspectsInvestigation()
BEGIN
    SELECT id, name, surname
    FROM Suspect
    WHERE height <= 170 AND surname LIKE 'Gre_n' AND name LIKE 'B%';
END