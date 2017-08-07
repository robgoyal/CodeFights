/* Name: projectsTeam.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the contributors of the project in ascending order
*/

CREATE PROCEDURE projectsTeam()
BEGIN
    SELECT DISTINCT name FROM projectLog ORDER BY name;
END