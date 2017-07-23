/* Name: volleyBallResults.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the results table in ascending order by the number
            of wins
*/

CREATE PROCEDURE volleyballResults()
BEGIN
    SELECT * FROM results ORDER BY wins;
END