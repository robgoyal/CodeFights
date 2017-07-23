/* Name: contestLeaderboard.sql
   Author: Robin Goyal
   Last-Modified: July 23, 2017
   Purpose: Return the participants with the 4th to 8th highest scores
*/

CREATE PROCEDURE contestLeaderboard()
BEGIN
    SELECT name
    FROM leaderboard
    ORDER BY score DESC
    LIMIT 3, 5;
END