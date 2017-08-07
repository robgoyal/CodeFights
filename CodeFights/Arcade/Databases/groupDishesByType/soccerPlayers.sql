/* Name: soccerPlayers.sql
   Author: Robin Goyal
   Last-Modified: August 7, 2017
   Purpose: Return a semicolon separated list of all the players sorted by
            their numbers in the format 'first_name surname #number'
*/

CREATE PROCEDURE soccerPlayers()
BEGIN
    SELECT GROUP_CONCAT(CONCAT_WS(' #', CONCAT_WS(' ', first_name, surname), player_number) ORDER BY player_number SEPARATOR '; ') AS players
    FROM soccer_team;
END