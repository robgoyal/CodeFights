/* Name: projectList.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the project name, team leads, and income ordered
            by id name
*/

CREATE PROCEDURE projetList()
BEGIN
    SELECT project_name, team_lead, income
    FROM Projects
    ORDER BY internal_id;
END