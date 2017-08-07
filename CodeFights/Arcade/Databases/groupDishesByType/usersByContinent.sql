/* Name: usersByContinent.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return the continent and the number of users from each continent
*/

CREATE PROCEDURE usersByContinent()
BEGIN
    SELECT continent, SUM(users) as users
    FROM countries
    GROUP BY continent
    ORDER BY users DESC;
END